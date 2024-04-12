import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer

# Load the dataset
df = pd.read_csv('archive_nba/Advanced.csv')

# Load the new dataset
df_per_game = pd.read_csv('archive_nba/Player Per Game.csv')

# Drop non-numerical columns
df_per_game_numeric = df_per_game.drop(['seas_id', 'season', 'player_id', 'player', 'birth_year', 'pos', 'lg', 'tm'], axis=1)

# Impute missing values with the median of the column
imputer = SimpleImputer(strategy='median')
df_per_game_imputed = pd.DataFrame(imputer.fit_transform(df_per_game_numeric), columns=df_per_game_numeric.columns)

# Normalize the data
sc = StandardScaler()
df_per_game_normalized = pd.DataFrame(sc.fit_transform(df_per_game_imputed), columns=df_per_game_imputed.columns)

# Merge the two datasets on 'player_id'
df_merged = pd.merge(df, df_per_game_normalized, on='player_id', suffixes=('_adv', '_per_game'))

# Drop non-numerical columns
df_numeric = df_merged.drop(['seas_id', 'season', 'player_id', 'player', 'birth_year', 'pos', 'lg', 'tm'], axis=1)

# Impute missing values with the median of the column
df_imputed = pd.DataFrame(imputer.fit_transform(df_numeric), columns=df_numeric.columns)

# Transform 'tov_percent' so that higher values are worse
df_imputed['tov_percent'] = -df_imputed['tov_percent']

# Drop 'age' and 'experience' columns
df_imputed = df_imputed.drop(['age', 'experience'], axis=1)

# Split the data into training and testing sets
# Assuming 'ws' (Win Shares) as the target column
X = df_imputed.drop('ws', axis=1)
y = df_imputed['ws']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Choose a model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Predict the 'ws' for each player in a given year
# For example, let's predict for the year 2020
# You need to load the original dataset again because 'season' and 'player' columns were dropped for model training
df_original = pd.read_csv('archive_nba/Advanced.csv')

# Preprocess the 2011 data in the same way as the training data
df_2011 = df_original[df_original['season'] == 2011]
df_2011_numeric = df_2011.drop(['seas_id', 'season', 'player', 'birth_year', 'pos', 'lg', 'tm'], axis=1)
df_2011_imputed = pd.DataFrame(imputer.transform(df_2011_numeric), columns=df_2011_numeric.columns)

# Add 'player_id' back to df_2011_imputed
df_2011_imputed['player_id'] = df_2011['player_id']

# Drop 'age' and 'experience' columns from df_2011_imputed
df_2011_imputed = df_2011_imputed.drop(['age', 'experience'], axis=1)

X_2011 = df_2011_imputed.drop('ws', axis=1)
X_2011 = sc.transform(X_2011)  # Normalize the data

# Predict 'ws' for 2011
ws_pred_2011 = model.predict(X_2011)

# Create a new DataFrame for 2011 predictions
df_2011_pred = df_2011.copy()
df_2011_pred['ws_pred'] = ws_pred_2011

# Find the player with the highest predicted 'ws'
best_player_2011 = df_original.loc[df_2011_pred['ws_pred'].idxmax(), 'player']
print('Best player for 2011:', best_player_2011)
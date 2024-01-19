# Jammming

## Purpose
Jammming is a web application that allows users to search for songs on the Spotify API and create custom playlists associated with their Spotify accounts. The purpose of this project is to provide users with a seamless and interactive way to discover music, curate playlists, and enjoy a personalized listening experience.

## Technologies Used
Jammming is built using the following technologies:

- **React:** A JavaScript library for building user interfaces.
- **Spotify API:** Used for fetching song data and managing user playlists.
- **HTML/CSS:** For structuring and styling the web application.
- **JavaScript:** For client-side scripting.
- **HTTP Requests and Responses:** To interact with the Spotify API.
- **Authentication:** Users can log in with their Spotify accounts.

## Features
1. **Search for Songs:**
   - Users can search for songs by song title.
   - Functionality to search by other attributes like artist’s name, genre, etc.

2. **View Song Information:**
   - Users can see information about each song like title, artist, and album for songs they queried.
   - Additional information design is customizable.

3. **Export Playlist to Spotify:**
   - Users can export their custom playlist to their personal Spotify account.

## Future Work
The following are some potential features to be added soon:

1. **Pressing Enter Triggers a Search:**
   - Allow users to initiate a search by pressing the "Enter" key, providing a more intuitive search experience.

2. **Preview Samples for Each Track:**
   - Include preview samples for each track in the search results, allowing users to listen to snippets before adding songs to their playlists.

3. **Display Only New Songs in Search Results:**
   - Modify the search results to display only songs that are not currently present in the user's playlist, reducing redundancy.

4. **Loading Screen During Playlist Saving:**
   - Add a loading screen or indicator to inform users while the playlist is being saved to their Spotify account.

5. **Optimize Access Token Logic:**
   - Update the access token logic to expire precisely at the right time, ensuring a seamless experience without unnecessary token refreshes.

6. **Restore Search Term After Redirect:**
   - After a user redirects on login, restore the search term from before the redirect, preserving the user's search context.

7. **Persist Playlist Information on Token Refresh:**
   - Ensure playlist information doesn’t get cleared if a user has to refresh their access token, maintaining a consistent user experience.

8. **Fetch and View Existing Playlists:**
   - Provide a way for users to fetch and view all their existing playlists, allowing for better organization and management.

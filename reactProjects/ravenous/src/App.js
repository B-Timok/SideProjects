import logo from './logo.svg';
import './App.css';
import BusinessList from './BusinessList';
import SearchBar from './SearchBar';
import Business from './Business';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>ravenous</h1>
      </header>
      <div className="App-body">
        <SearchBar />
        <BusinessList />  
      </div>
    </div>
  );
}

export default App;

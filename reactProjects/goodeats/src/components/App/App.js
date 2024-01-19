import React, { useState } from "react";
import styles from "./App.module.css";

import BusinessList from "../BusinessList/BusinessList";
import SearchBar from "../SearchBar/SearchBar";
import Yelp from "../../utils/Yelp";

function App() {

  const [businesses, setBusinesses] = useState([]);

  const searchYelp = async (searchTerm, location, sortBy) => {
    const businesses = await Yelp.search(searchTerm, location, sortBy);
    setBusinesses(businesses);
  };

  return (
    <div className={styles.App}>
      <h1>goodeats</h1>
      <SearchBar searchYelp={searchYelp} />
      <BusinessList businesses={businesses} />
    </div>
  );
};

export default App;

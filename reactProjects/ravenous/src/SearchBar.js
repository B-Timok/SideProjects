import React, { useState } from 'react';
import './SearchBar.css';

function SearchBar() {
    const [searchTerm, setSearchTerm] = useState('');
    const [location, setLocation] = useState('');
    const [sortOption, setSortOption] = useState('best_match');

    const handleSearch = () => {
        // Implement search functionality here
        console.log('Search term:', searchTerm);
        console.log('Location:', location);
        console.log('Sort option:', sortOption);
    };

    return (
        <div className="SearchBar">
            <div className="SearchBar-sort-options">
                <button
                    className={sortOption === 'best_match' ? 'active' : ''}
                    onClick={() => setSortOption('best_match')}
                >
                    Best<br />Match
                </button>
                <button
                    className={sortOption === 'rating' ? 'active' : ''}
                    onClick={() => setSortOption('rating')}
                >
                    Highest<br />Rated
                </button>
                <button
                    className={sortOption === 'review_count' ? 'active' : ''}
                    onClick={() => setSortOption('review_count')}
                >
                    Most<br />Reviewed
                </button>
            </div>
            <div className="SearchBar-fields">
                <input
                    placeholder="Search Businesses"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />
                <input
                    placeholder="Where?"
                    value={location}
                    onChange={(e) => setLocation(e.target.value)}
                />
            </div>
            <div className="SearchBar-submit">
                <button onClick={handleSearch}>Let's Go</button>
            </div>
        </div>
    );
};

export default SearchBar;
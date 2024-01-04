import React from 'react';
import './Business.css';

const business = {
    imageSrc: 'https://via.placeholder.com/150',
    name: 'Restaurant Name',
    address: '1234 Street Rd',
    city: 'City',
    state: 'ST',
    zipCode: '12345',
    category: 'CATEGORY',
    rating: 4.5,
    reviewCount: 90
};

function Business() {
    return (
        <div className="Business">
            <div className="image-container">
                <img src={business.imageSrc} alt=''/>
            </div>
            <h2>Restaurant Name</h2>
            <div className="Business-information">
                <div className="Business-address">
                    <p>{business.address}</p>
                    <p>{business.city}</p>
                    <p>{`${business.state}, ${business.zipCode}`}</p>
                </div>
                <div className="Business-reviews">
                    <p>{business.category}</p>
                    <p>{business.rating}</p>
                    <p className='Business-reviewCount'>{`${business.reviewCount} reviews`}</p>
                </div>
            </div>
        </div>
    );
}

export default Business;
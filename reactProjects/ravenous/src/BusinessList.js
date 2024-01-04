import React from 'react';
import './BusinessList.css';
import Business from './Business';

const businesses = [
    {
        imageSrc: 'https://via.placeholder.com/150',
        name: 'Restaurant Name',
        address: '1234 Street Rd',
        city: 'City',
        state: 'ST',
        zipCode: '12345',
        category: 'CATEGORY',
        rating: 4.5,
        reviewCount: 90
    },

    {
        imageSrc: 'https://via.placeholder.com/150',
        name: 'Restaurant Name',
        address: '1234 Street Rd',
        city: 'City',
        state: 'ST',
        zipCode: '12345',
        category: 'CATEGORY',
        rating: 4.5,
        reviewCount: 90
    },

    {
        imageSrc: 'https://via.placeholder.com/150',
        name: 'Restaurant Name',
        address: '1234 Street Rd',
        city: 'City',
        state: 'ST',
        zipCode: '12345',
        category: 'CATEGORY',
        rating: 4.5,
        reviewCount: 90
    },

    {
        imageSrc: 'https://via.placeholder.com/150',
        name: 'Restaurant Name',
        address: '1234 Street Rd',
        city: 'City',
        state: 'ST',
        zipCode: '12345',
        category: 'CATEGORY',
        rating: 4.5,
        reviewCount: 90
    },

    {
        imageSrc: 'https://via.placeholder.com/150',
        name: 'Restaurant Name',
        address: '1234 Street Rd',
        city: 'City',
        state: 'ST',
        zipCode: '12345',
        category: 'CATEGORY',
        rating: 4.5,
        reviewCount: 90
    },

    {
        imageSrc: 'https://via.placeholder.com/150',
        name: 'Restaurant Name',
        address: '1234 Street Rd',
        city: 'City',
        state: 'ST',
        zipCode: '12345',
        category: 'CATEGORY',
        rating: 4.5,
        reviewCount: 90
    }
];

function BusinessList() {
    return (
        <div className="BusinessList">
            {
                businesses.map((business, index) => {
                    return <Business key={index} business={business} />
                })
            }
        </div>
    );
}

export default BusinessList;
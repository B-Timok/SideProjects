import React from "react";
import styles from "./BusinessList.module.css";

import Business from "../Business/Business";

function BusinessList(props) {
  const businesses = props.businesses;

  return (
    <div className={styles.BusinessList}>
      {businesses.map((business, index) => (
        <Business key={index} business={business} />
      ))}
    </div>
  );
};

export default BusinessList;

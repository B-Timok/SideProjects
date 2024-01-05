import React from "react";
import styles from "./BusinessList.module.css";

import Business from "../Business/Business";

function BusinessList() {
  return (
    <div className={styles.BusinessList}>
      <Business />
      <Business />
      <Business />
      <Business />
      <Business />
      <Business />
      <Business />
      <Business />
    </div>
  );
};

export default BusinessList;

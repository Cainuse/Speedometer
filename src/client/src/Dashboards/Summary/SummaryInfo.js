import React from "react";
import { Typography } from "@material-ui/core";

const SummaryInfo = ({ totalVal, totalText, highestVal, highestText }) => {
  return (
    <div>
      <div>
        <Typography variant="h1">{totalVal}</Typography>
        <Typography variant="subtitle1">{totalText}</Typography>
      </div>
      <br />
      <div>
        <Typography variant="h1">{highestVal}</Typography>
        <Typography variant="subtitle1">{highestText}</Typography>
      </div>
    </div>
  );
};

export default SummaryInfo;

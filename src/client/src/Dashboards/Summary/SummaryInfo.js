import React from "react";
import { Typography } from "@material-ui/core";

const SummaryInfo = ({
  totalVal,
  totalText,
  highestVal,
  highestText,
  type,
}) => {
  return (
    <div>
      <Typography variant="h1" style={{ fontSize: "5rem" }}>
        {totalVal}
        <Typography variant="h5" style={{ display: "inline-block" }}>
          {type === "memory" ? "kb" : "ms"}
        </Typography>
      </Typography>
      <Typography variant="subtitle1">{totalText}</Typography>
      <br />
      <br />
      <Typography variant="h1" style={{ fontSize: "5rem" }}>
        {highestVal}
      </Typography>
      <Typography variant="subtitle1">{highestText}</Typography>
    </div>
  );
};

export default SummaryInfo;

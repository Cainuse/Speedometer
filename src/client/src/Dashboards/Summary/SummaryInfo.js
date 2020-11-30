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
      <Typography variant="h1" style={{ fontSize: "8rem" }}>
        {totalVal}
        <Typography variant="h5" style={{ display: "inline-block" }}>
          {type === "memory" ? "mb" : "ms"}
        </Typography>
      </Typography>
      <Typography variant="subtitle1">{totalText}</Typography>
      {highestVal && highestVal !== "" ? (
        <div>
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <Typography variant="h2" style={{ fontSize: "6rem" }}>
            {highestVal}
          </Typography>
          <Typography variant="subtitle1">{highestText}</Typography>
        </div>
      ) : null}
    </div>
  );
};

export default SummaryInfo;

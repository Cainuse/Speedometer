import React from "react";
import { Sankey, Tooltip } from "recharts";
import SankeyLink from "./SankeyLink";
import SankeyNode from "./SankeyNode";
import { Typography } from "@material-ui/core";
import Paper from "@material-ui/core/Paper";

const ScriptSankeyChart = ({ data, type }) => {
  const isInvalidData = (data) => {
    const nodes = data["nodes"];
    const links = data["links"];
    return (
      nodes === undefined ||
      links === undefined ||
      nodes.length === 0 ||
      links.length === 0
    );
  };

  return isInvalidData ? null : (
    <Paper elevation={5}>
      <Typography variant="subtitle1">
        {`Sankey Chart representing ${type} distribution broken down by classes
        and functions`}
      </Typography>

      <Sankey
        width={1330}
        height={800}
        margin={{ top: 20, bottom: 20 }}
        data={data}
        nodeWidth={15}
        nodePadding={50}
        linkCurvature={0.5}
        iterations={25}
        link={<SankeyLink />}
        node={<SankeyNode containerWidth={960} />}
      >
        <defs>
          <linearGradient id={"linkGradient"}>
            <stop offset="0%" stopColor="rgba(0, 136, 254, 0.5)" />
            <stop offset="100%" stopColor="rgba(0, 197, 159, 0.3)" />
          </linearGradient>
        </defs>
        <Tooltip />
      </Sankey>
    </Paper>
  );
};

export default ScriptSankeyChart;

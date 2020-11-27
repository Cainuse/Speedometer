import React from "react";
import { Sankey, Tooltip } from "recharts";
import SankeyLink from "./SankeyLink";
import SankeyNode from "./SankeyNode";

function ScriptSankeyChart({ data }) {
  return (
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
  );
}

export default ScriptSankeyChart;

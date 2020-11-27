import React, { PureComponent } from "react";
import {
  PieChart,
  Pie,
  Cell,
  Legend,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import { getRandomColor } from "../../../constants";

const RADIAN = Math.PI / 180;
const renderCustomizedLabel = ({
  cx,
  cy,
  midAngle,
  innerRadius,
  outerRadius,
  percent,
}) => {
  const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
  const x = cx + radius * Math.cos(-midAngle * RADIAN);
  const y = cy + radius * Math.sin(-midAngle * RADIAN);

  return (
    <text
      x={x}
      y={y}
      fill="white"
      textAnchor={x > cx ? "start" : "end"}
      dominantBaseline="central"
    >
      {`${(percent * 100).toFixed(0)}%`}
    </text>
  );
};

export default class FunctionsPieChart extends PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      colors: this.props.data.map((d) => {
        return getRandomColor();
      }),
    };
  }

  render() {
    return (
      <ResponsiveContainer width="100%" height="100%">
        <PieChart margin={{ left: 50, bottom: 50 }}>
          <Pie
            data={this.props.data}
            cx={200}
            cy={200}
            labelLine={false}
            label={renderCustomizedLabel}
            innerRadius={70}
            outerRadius={160}
            fill="#8884d8"
            dataKey={this.props.pieDataKey}
          >
            {this.props.data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={this.state.colors[index]} />
            ))}
          </Pie>
          <Tooltip />
          <Legend layout="vertical" verticalAlign="middle" align="right" />
        </PieChart>
      </ResponsiveContainer>
    );
  }
}

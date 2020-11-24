import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import { Box, Typography } from "@material-ui/core";
import MemoryAreaChart from "../Visualizations/MemoryAreaChart";
import FunctionsPieChart from "../Visualizations/FunctionsPieChart";
import ComposedBarChart from "../Visualizations/ComposedBarChart";
import ScriptSankeyChart from "../Visualizations/ScriptSankeyChart";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(3),
    textAlign: "center",
    color: theme.palette.text.secondary,
    height: "25rem",
  },
}));

const nDataX = "n";
const nDataY = "script_memory";

const nData = [
  { [nDataX]: 1, [nDataY]: 4.11 },
  { [nDataX]: 3, [nDataY]: 2.39 },
  { [nDataX]: 5, [nDataY]: 1.37 },
  { [nDataX]: 4, [nDataY]: 1.16 },
  { [nDataX]: 9, [nDataY]: 2.29 },
  { [nDataX]: 11, [nDataY]: 3.22 },
  { [nDataX]: 10, [nDataY]: 4.11 },
  { [nDataX]: 15, [nDataY]: 4.81 },
  { [nDataX]: 14, [nDataY]: 19.11 },
  { [nDataX]: 19, [nDataY]: 88.11 },
  { [nDataX]: 21, [nDataY]: 32.11 },
];

const fnDataX = "name";
const fnDataY = "space_usage";

const fnData = [
  { [fnDataX]: "foo1()", [fnDataY]: 0.2 },
  { [fnDataX]: "foo2()", [fnDataY]: 0.3 },
  { [fnDataX]: "foo3()", [fnDataY]: 0.4 },
  { [fnDataX]: "foo4()", [fnDataY]: 0.5 },
  { [fnDataX]: "foo5()", [fnDataY]: 0.8 },
  { [fnDataX]: "foo6()", [fnDataY]: 0.9 },
  { [fnDataX]: "foo7()", [fnDataY]: 0.2 },
  { [fnDataX]: "foo8()", [fnDataY]: 0.6 },
];

const SpaceComplexity = () => {
  const classes = useStyles();

  const defaultProps = {
    bgcolor: "background.paper",
    m: 1,
    style: { width: "100%", height: "2rem", marginBottom: "3%" },
    borderColor: "grey.500",
  };

  return (
    <div className={classes.root}>
      <Box borderBottom={1} {...defaultProps}>
        Space Complexity Analysis for 'test.py'
      </Box>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <Typography>Memory Usage Area Chart</Typography>
            <MemoryAreaChart data={nData} xDataKey={nDataX} yDataKey={nDataY} />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.paper}>
            <Typography>Memory Usage Per Function Pie Chart</Typography>
            <FunctionsPieChart data={fnData} pieDataKey={fnDataY} />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.paper}>
            <Typography>Memory Usage Per Function Bar Chart</Typography>
            <ComposedBarChart data={fnData} barDataKey={fnDataY} />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={12}>
          <Typography>Space Usage Per Script module</Typography>
          <ScriptSankeyChart />
        </Grid>
      </Grid>
    </div>
  );
};

export default SpaceComplexity;

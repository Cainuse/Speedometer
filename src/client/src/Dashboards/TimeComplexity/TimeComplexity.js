import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import { Box, Typography } from "@material-ui/core";
import ComplexityTimeLine from "../Visualizations/ComplexityTimeLine";
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
    justifyContent: "center",
    height: "25rem",
  },
  timeline_paper: {
    padding: theme.spacing(3),
    textAlign: "center",
    color: theme.palette.text.secondary,
    justifyContent: "center",
  },
}));

const data = [
  {
    time: "00:00",
    fn: "foo()",
  },
  {
    time: "00:05",
    fn: "bar()",
  },
  {
    time: "00:10",
    fn: "bla1()",
  },
  {
    time: "00:15",
    fn: "bla2()",
  },
  {
    time: "00:20",
    fn: "bla3()",
  },
  {
    time: "00:25",
    fn: "bla4()",
  },
  {
    time: "00:30",
    fn: "bla5()",
  },
  {
    time: "00:40",
    fn: "bla6()",
  },
  {
    time: "00:59",
    fn: "bla7()",
  },
];

const fnDataX = "name";
const fnDataY = "time_proportion";

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

const TimeComplexity = () => {
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
        Time Complexity Analysis for 'test.py'
      </Box>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.timeline_paper}>
            <Typography>Script Execution Timeline</Typography>
            <ComplexityTimeLine data={data} />
          </Paper>
        </Grid>
        <Grid container item xs={12} sm={6} spacing={3}>
          <Grid item xs={12}>
            <Paper className={classes.paper}>
              <Typography>Relative Time Per Function Pie Chart</Typography>
              <FunctionsPieChart data={fnData} pieDataKey={fnDataY} />
            </Paper>
          </Grid>
          <Grid item xs={12}>
            <Paper className={classes.paper}>
              <Typography>Relative Time Per Function Bar Chart</Typography>
              <ComposedBarChart data={fnData} barDataKey={fnDataY} />
            </Paper>
          </Grid>
        </Grid>
        <Grid item xs={12} sm={12}>
          <Typography>Relative Time Per Script module</Typography>
          <ScriptSankeyChart />
        </Grid>
      </Grid>
    </div>
  );
};

export default TimeComplexity;

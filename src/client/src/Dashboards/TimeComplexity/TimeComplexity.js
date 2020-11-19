import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import { Box } from "@material-ui/core";
import ComplexityTimeLine from "../Visualizations/ComplexityTimeLine";
import FunctionsPieChart from "../Visualizations/FunctionsPieChart";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
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
    fn: "bla()",
  },
  {
    time: "00:10",
    fn: "bla()",
  },
  {
    time: "00:10",
    fn: "bla()",
  },
  {
    time: "00:10",
    fn: "bla()",
  },
  {
    time: "00:10",
    fn: "bla()",
  },
  {
    time: "00:10",
    fn: "bla()",
  },
  {
    time: "00:10",
    fn: "bla()",
  },
];

const fnData = [
  { name: "foo1()", value: 0.2 },
  { name: "foo2()", value: 0.4 },
  { name: "bar1()", value: 0.1 },
  { name: "bar2()", value: 0.1 },
  { name: "bla1()", value: 0.1 },
  { name: "bla2()", value: 0.1 },
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
          <Paper className={classes.paper}>
            <ComplexityTimeLine data={data} />
          </Paper>
        </Grid>
        <Grid container item xs={12} sm={6}>
          <Grid item xs={12}>
            <Paper className={classes.paper}>
              <FunctionsPieChart data={fnData} />
            </Paper>
          </Grid>
          <Grid item xs={12}>
            <Paper className={classes.paper}>
              Script big-O time complexity line chart
              {/* TODO: Make a card with proper titles,
            descrition, maybe buttons for interactions,
            properly formatted */}
            </Paper>
          </Grid>
          <Grid item xs={12}>
            <Paper className={classes.paper}>
              Runtime per module SankeyChart
              {/* TODO: Make a card with proper titles,
            descrition, maybe buttons for interactions,
            properly formatted */}
            </Paper>
          </Grid>
        </Grid>
      </Grid>
    </div>
  );
};

export default TimeComplexity;

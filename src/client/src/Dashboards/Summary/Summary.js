import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import { Box } from "@material-ui/core";
import Speedometer from "./Speedometer";
import SummaryInfo from "./SummaryInfo";
import PerfLineChart from "../Visualizations/PerfLineChart";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    textAlign: "center",
    color: theme.palette.text.secondary,
    height: "100%",
  },
  viz_container: {
    padding: theme.spacing(2),
    height: "120vh",
  },
  fullHeight: {
    height: "100%",
  },
  halfHeight: {
    height: "50%",
  },
}));

const data = [
  { n: 1, myScript: 4.11, "O(1)": 5.6, "O(n)": 7.8 },
  { n: 3, myScript: 2.39, "O(1)": 3.6, "O(n)": 8.8 },
  { n: 5, myScript: 1.37, "O(1)": 2.6, "O(n)": 9.8 },
  { n: 4, myScript: 1.16, "O(1)": 1.6, "O(n)": 10.8 },
  { n: 9, myScript: 2.29, "O(1)": 6.6, "O(n)": 11.8 },
  { n: 11, myScript: 3.22, "O(1)": 7.6, "O(n)": 12.8 },
  { n: 10, myScript: 4.11, "O(1)": 5.6, "O(n)": 7.8 },
  { n: 15, myScript: 4.81, "O(1)": 7.96, "O(n)": 47.8 },
  { n: 14, myScript: 19.11, "O(1)": 43.6, "O(n)": 7.8 },
  { n: 19, myScript: 88.11, "O(1)": 32.6, "O(n)": 12.8 },
  { n: 21, myScript: 32.11, "O(1)": 91.6, "O(n)": 22.8 },
];

const Summary = () => {
  const classes = useStyles();

  const defaultProps = {
    bgcolor: "background.paper",
    m: 1,
    style: { width: "100%", height: "2rem", marginBottom: "1%" },
    borderColor: "grey.500",
  };

  return (
    <div className={classes.root}>
      <Box borderBottom={1} {...defaultProps}>
        Performance Summary for 'test.py'
      </Box>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.viz_container}>
            <Grid container spacing={3} className={classes.fullHeight}>
              <Grid item xs={12} className={classes.halfHeight}>
                <Paper className={classes.paper}>
                  <Speedometer value={5.5} valueText="Time Complexity" />
                </Paper>
              </Grid>
              <Grid item xs={12} className={classes.halfHeight}>
                <Paper className={classes.paper}>
                  <Speedometer value={3.5} valueText="Space Complexity" />
                </Paper>
              </Grid>
            </Grid>
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.viz_container}>
            <Grid container spacing={3} className={classes.fullHeight}>
              <Grid item xs={12} className={classes.halfHeight}>
                <Paper className={classes.paper}>
                  <SummaryInfo
                    totalVal="4.5s"
                    totalText="Total Runtime"
                    highestVal="bar()"
                    highestText="Highest Runtime Function"
                  />
                </Paper>
              </Grid>
              <Grid item xs={12} className={classes.halfHeight}>
                <Paper className={classes.paper}>
                  <SummaryInfo
                    totalVal="29kb"
                    totalText="Total Memory Usage"
                    highestVal="foo()"
                    highestText="Highest Memory Usage Function"
                  />
                </Paper>
              </Grid>
            </Grid>
          </Paper>
        </Grid>
        <Grid item xs={12}>
          <Paper className={classes.viz_container}>
            <Grid container spacing={3} className={classes.fullHeight}>
              <Grid item xs={12} className={classes.halfHeight}>
                <Paper className={classes.paper}>
                  <PerfLineChart data={data} yLabel="Time (ms)" yUnit="ms" />
                </Paper>
              </Grid>
              <Grid item xs={12} className={classes.halfHeight}>
                <Paper className={classes.paper}>
                  <PerfLineChart data={data} yLabel="Memory (KB)" yUnit="kb" />
                </Paper>
              </Grid>
            </Grid>
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
};

export default Summary;

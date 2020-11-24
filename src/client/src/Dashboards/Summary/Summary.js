import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { connect } from "react-redux";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import { Box, Typography } from "@material-ui/core";
import Speedometer from "./Speedometer";
import SummaryInfo from "./SummaryInfo";
import PerfLineChart from "../Visualizations/Line/PerfLineChart";

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
    height: "50rem",
  },
  fullHeight: {
    height: "100%",
  },
  halfHeight: {
    height: "50%",
  },
}));

const Summary = ({ dataset }) => {
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
        <Grid item xs={4} className={classes.viz_container}>
          <Grid container spacing={3} className={classes.fullHeight}>
            <Grid item xs={12} className={classes.halfHeight}>
              <Paper className={classes.paper}>
                <Typography>Time Complexity Speedometer</Typography>
                <Speedometer value={5.5} valueText="Time Complexity" />
              </Paper>
            </Grid>
            <Grid item xs={12} className={classes.halfHeight}>
              <Paper className={classes.paper}>
                <Typography>Space Complexity Speedometer</Typography>
                <Speedometer value={3.5} valueText="Space Complexity" />
              </Paper>
            </Grid>
          </Grid>
        </Grid>
        <Grid item xs={2} className={classes.viz_container}>
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
        </Grid>
        <Grid item xs={6} className={classes.viz_container}>
          <Grid container spacing={3} className={classes.fullHeight}>
            <Grid item xs={12} className={classes.halfHeight}>
              <Paper className={classes.paper}>
                <PerfLineChart
                  data={dataset["e2e"]["e2e_runtime"]}
                  yLabel="Time (ms)"
                  yUnit="ms"
                />
              </Paper>
            </Grid>
            <Grid item xs={12} className={classes.halfHeight}>
              <Paper className={classes.paper}>
                <PerfLineChart
                  data={dataset["e2e"]["e2e_memory"]}
                  yLabel="Memory (KB)"
                  yUnit="kb"
                />
              </Paper>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    dataset: state.dataset,
  };
};

export default connect(mapStateToProps)(Summary);

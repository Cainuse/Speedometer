import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { connect } from "react-redux";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import { Box, Typography } from "@material-ui/core";
import Speedometer from "./Speedometer";
import SummaryInfo from "./SummaryInfo";
import PerfLineChart from "../Visualizations/Line/PerfLineChart";
import InfoPopup from "./InfoPopup";

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
    height: "52rem",
  },
  fullHeight: {
    height: "100%",
  },
  halfHeight: {
    height: "50%",
  },
  card_title: {
    paddingLeft: "15%",
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

  const getSpeedometerVal = (complexity) => {
    const speedometerVals = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5];
    switch (complexity) {
      case "nn":
        return speedometerVals[0];
      case "n!":
        return speedometerVals[1];
      case "n3":
        return speedometerVals[2];
      case "n2":
        return speedometerVals[3];
      case "nlogn":
        return speedometerVals[4];
      case "n":
        return speedometerVals[5];
      case "logn":
        return speedometerVals[6];
      case "1":
        return speedometerVals[7];
      default:
        return 0;
    }
  };

  return (
    <div className={classes.root}>
      <Box borderBottom={1} {...defaultProps}>
        Performance Summary for {dataset["script_name"]}
      </Box>
      <Grid container spacing={3}>
        <Grid item xs={4} className={classes.viz_container}>
          <Grid container spacing={3} className={classes.fullHeight}>
            <Grid item xs={12} className={classes.halfHeight}>
              <Paper className={classes.paper} elevation={5}>
                <Grid container>
                  <Grid item xs={11} className={classes.card_title}>
                    <Typography>Time Complexity Speedometer </Typography>
                  </Grid>
                  <Grid item xs={1}>
                    <InfoPopup
                      content="This Speedometer shows the average time complexity of your
                  script."
                    />
                  </Grid>
                </Grid>
                <Speedometer
                  value={getSpeedometerVal(
                    dataset["e2e"]["e2e_time_complexity"]
                  )}
                  valueText="Time Complexity"
                />
              </Paper>
            </Grid>
            <Grid item xs={12} className={classes.halfHeight}>
              <Paper className={classes.paper} elevation={5}>
                <Grid container>
                  <Grid item xs={11} className={classes.card_title}>
                    <Typography>Space Complexity Speedometer</Typography>
                  </Grid>
                  <Grid item xs={1}>
                    <InfoPopup content="This Speedometer shows the average memory usage complexity of your script." />
                  </Grid>
                </Grid>
                <Speedometer
                  value={getSpeedometerVal(
                    dataset["e2e"]["e2e_space_complexity"]
                  )}
                  valueText="Space Complexity"
                />
              </Paper>
            </Grid>
          </Grid>
        </Grid>
        <Grid item xs={2} className={classes.viz_container}>
          <Grid container spacing={3} className={classes.fullHeight}>
            <Grid item xs={12} className={classes.halfHeight}>
              <Paper className={classes.paper} elevation={5}>
                <SummaryInfo
                  totalVal={dataset["e2e"]["e2e_total_average_time"].toString()}
                  totalText="Total Average Runtime"
                  highestVal={dataset["e2e"]["e2e_highest_runtime_function"]}
                  highestText="Highest Runtime Function"
                  type="runtime"
                />
              </Paper>
            </Grid>
            <Grid item xs={12} className={classes.halfHeight}>
              <Paper className={classes.paper} elevation={5}>
                <SummaryInfo
                  totalVal={dataset["e2e"][
                    "e2e_total_average_memory"
                  ].toString()}
                  totalText="Total Average Memory Usage"
                  highestVal={
                    dataset["e2e"]["e2e_highest_memory_usage_function"]
                  }
                  highestText="Highest Memory Usage Function"
                  type="memory"
                />
              </Paper>
            </Grid>
          </Grid>
        </Grid>
        <Grid item xs={6} className={classes.viz_container}>
          <Grid container spacing={3} className={classes.fullHeight}>
            <Grid item xs={12} className={classes.halfHeight}>
              <Paper className={classes.paper} elevation={5}>
                <PerfLineChart
                  data={dataset["e2e"]["e2e_runtime"]}
                  yLabel="Time (ms)"
                  yUnit="ms"
                />
              </Paper>
            </Grid>
            <Grid item xs={12} className={classes.halfHeight}>
              <Paper className={classes.paper} elevation={5}>
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

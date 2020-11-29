import React from "react";
import { connect } from "react-redux";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import { Box, Typography } from "@material-ui/core";
import MemoryAreaChart from "../Visualizations/Area/MemoryAreaChart";
import FunctionsPieChart from "../Visualizations/Pie/FunctionsPieChart";
import ComposedBarChart from "../Visualizations/Bar/ComposedBarChart";
import ScriptSankeyChart from "../Visualizations/Sankey/ScriptSankeyChart";
import { getFilteredInputData } from "../../constants";
import InfoPopup from "../Visualizations/Popup/InfoPopup";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(3),
    textAlign: "center",
    color: theme.palette.text.secondary,
    height: "27rem",
  },
  card_title: {
    paddingLeft: "10%",
  },
  info_content: {
    width: "20rem",
    wordWrap: "break-word",
  },
}));

const nDataX = "n";
const nDataY = "total_memory";
const fnDataY = "total_memory";

const SpaceComplexity = ({ dataset }) => {
  const classes = useStyles();

  const nData = getFilteredInputData(dataset, "e2e_memory");

  const defaultProps = {
    bgcolor: "background.paper",
    m: 1,
    style: { width: "100%", height: "2rem", marginBottom: "1%" },
    borderColor: "grey.500",
  };

  return (
    <div className={classes.root}>
      <Box borderBottom={1} {...defaultProps}>
        Space Complexity Analysis for 'test.py'
      </Box>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.paper} elevation={5}>
            <Grid container>
              <Grid item xs={11} className={classes.card_title}>
                <Typography>Memory Usage Area Chart</Typography>
              </Grid>
              <Grid item xs={1}>
                <InfoPopup
                  anchorOrigin={{
                    vertical: "bottom",
                    horizontal: "right",
                  }}
                  transformOrigin={{
                    vertical: "top",
                    horizontal: "right",
                  }}
                  content={
                    <Typography className={classes.info_content}>
                      This area chart shows total memory usage of your script
                      for each input size n.
                    </Typography>
                  }
                />
              </Grid>
            </Grid>
            <MemoryAreaChart data={nData} xDataKey={nDataX} yDataKey={nDataY} />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.paper} elevation={5}>
            <Grid container>
              <Grid item xs={11} className={classes.card_title}>
                <Typography>Memory Usage Per Function Pie Chart</Typography>
              </Grid>
              <Grid item xs={1}>
                <InfoPopup
                  anchorOrigin={{
                    vertical: "bottom",
                    horizontal: "right",
                  }}
                  transformOrigin={{
                    vertical: "top",
                    horizontal: "right",
                  }}
                  content={
                    <Typography className={classes.info_content}>
                      This pie chart shows the proportion of memory usage for
                      each of the functions in your script relative to the
                      overall script memory consumption.
                    </Typography>
                  }
                />
              </Grid>
            </Grid>
            <FunctionsPieChart
              data={dataset["function"]["function_memory"]}
              pieDataKey={fnDataY}
            />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.paper} elevation={5}>
            <Grid container>
              <Grid item xs={11} className={classes.card_title}>
                <Typography>Memory Usage Per Function Bar Chart</Typography>
              </Grid>
              <Grid item xs={1}>
                <InfoPopup
                  anchorOrigin={{
                    vertical: "bottom",
                    horizontal: "right",
                  }}
                  transformOrigin={{
                    vertical: "top",
                    horizontal: "right",
                  }}
                  content={
                    <Typography className={classes.info_content}>
                      This bar chart shows the proportion of memory usage for
                      each of the functions in your script for purposes of
                      comparison and analysis.
                    </Typography>
                  }
                />
              </Grid>
            </Grid>
            <ComposedBarChart
              data={dataset["function"]["function_memory"]}
              barDataKey={fnDataY}
              yLabel="Total Memory (mb)"
            />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={12}>
          <ScriptSankeyChart
            data={dataset["sankey"]["sankey_runtime"]}
            type="memory usage"
          />
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

export default connect(mapStateToProps)(SpaceComplexity);

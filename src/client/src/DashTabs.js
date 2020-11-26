import React, { useState } from "react";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Box from "@material-ui/core/Box";
import Summary from "./Dashboards/Summary/Summary";
import SpaceComplexity from "./Dashboards/SpaceComplexity/SpaceComplexity";
import TimeComplexity from "./Dashboards/TimeComplexity/TimeComplexity";
import LineByLineComplexity from "./Dashboards/LineByLine/LineByLineComplexity";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
  },
  tabs_appbar: {
    backgroundColor: "#66d9ff",
  },
}));

const DashTabs = () => {
  const classes = useStyles();
  const [value, setValue] = useState(0);

  const handleChange = (_, newValue) => {
    setValue(newValue);
  };

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.tabs_appbar}>
        <Tabs
          variant="fullWidth"
          value={value}
          onChange={handleChange}
          aria-label="nav tabs example"
        >
          <LinkTab
            variant="h5"
            label="Summary"
            href="/summary"
            {...LinkTabProps(0)}
          />
          <LinkTab
            label="Time Complexity"
            href="/timeComplexity"
            {...LinkTabProps(1)}
          />
          <LinkTab
            label="Space Complexity"
            href="/spaceComplexity"
            {...LinkTabProps(2)}
          />
          <LinkTab
            label="Line By Line"
            href="/lineByLineComplexity"
            {...LinkTabProps(3)}
          />
        </Tabs>
      </AppBar>
      <TabPanel value={value} index={0}>
        <Summary />
      </TabPanel>
      <TabPanel value={value} index={1}>
        <TimeComplexity />
      </TabPanel>
      <TabPanel value={value} index={2}>
        <SpaceComplexity />
      </TabPanel>
      <TabPanel value={value} index={3}>
        <LineByLineComplexity />
      </TabPanel>
    </div>
  );
};

const TabPanel = (props) => {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`nav-tabpanel-${index}`}
      aria-labelledby={`nav-tab-${index}`}
      {...other}
    >
      {value === index && <Box p={5}>{children}</Box>}
    </div>
  );
};

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

const LinkTabProps = (index) => {
  return {
    id: `nav-tab-${index}`,
    "aria-controls": `nav-tabpanel-${index}`,
    style: {
      textTransform: "none",
      fontSize: "1.2rem",
      color: "white",
    },
  };
};

const LinkTab = (props) => {
  return (
    <Tab
      component="a"
      onClick={(event) => {
        event.preventDefault();
      }}
      {...props}
    />
  );
};

export default DashTabs;

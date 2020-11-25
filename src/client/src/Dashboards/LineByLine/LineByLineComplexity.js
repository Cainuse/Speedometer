import React, { useState, useEffect } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { connect } from "react-redux";
import Accordion from "@material-ui/core/Accordion";
import AccordionSummary from "@material-ui/core/AccordionSummary";
import AccordionDetails from "@material-ui/core/AccordionDetails";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import { Box, Typography } from "@material-ui/core";
import SyntaxHighlighter from "react-syntax-highlighter";
import { gruvboxLight } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { Grid } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular,
  },
}));

const LineByLineComplexity = ({ codeInformations, dataset }) => {
  const classes = useStyles();

  let expandedAcords = [];
  for (let i = 0; i < codeInformations.length; i++) {
    expandedAcords.push(true);
  }

  const [expanded, setExpanded] = useState(expandedAcords);

  const defaultProps = {
    bgcolor: "background.paper",
    m: 1,
    style: { width: "100%", height: "2rem", marginBottom: "1%" },
    borderColor: "grey.500",
  };

  const handleChange = (idx) => (_event, _isExpanded) => {
    let expansions = [...expanded];
    expansions[idx] = !expansions[idx];
    setExpanded(expansions);
  };

  return (
    <div className={classes.root}>
      <Box borderBottom={1} {...defaultProps}>
        Line by Line Analysis for {dataset["script_name"]}
      </Box>
      <Grid container spacing={3}>
        {codeInformations.map((info, index) => {
          return (
            <Grid item xs={6}>
              <Accordion
                expanded={expanded[index]}
                onChange={handleChange(index)}
                elevation={5}
              >
                <AccordionSummary
                  expandIcon={<ExpandMoreIcon />}
                  aria-controls="panel1a-content"
                  id={`panel-${index}-header`}
                >
                  <Typography
                    className={classes.heading}
                  >{`Script Part ${index}`}</Typography>
                </AccordionSummary>
                <AccordionDetails>
                  <Typography>
                    <Typography
                      variant="h2"
                      color={info.proportion > 0.2 ? "error" : "primary"}
                    >
                      {(info.proportion * 100).toString() + "%"}
                    </Typography>
                    <SyntaxHighlighter language="python" style={gruvboxLight}>
                      {info.code}
                    </SyntaxHighlighter>
                  </Typography>
                </AccordionDetails>
              </Accordion>
            </Grid>
          );
        })}
      </Grid>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    dataset: state.dataset,
  };
};

export default connect(mapStateToProps)(LineByLineComplexity);

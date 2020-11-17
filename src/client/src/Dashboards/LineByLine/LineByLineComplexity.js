import React, { useState, useEffect } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Accordion from "@material-ui/core/Accordion";
import AccordionSummary from "@material-ui/core/AccordionSummary";
import AccordionDetails from "@material-ui/core/AccordionDetails";
import Typography from "@material-ui/core/Typography";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import SyntaxHighlighter from "react-syntax-highlighter";
import { darcula } from "react-syntax-highlighter/dist/esm/styles/hljs";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular,
  },
}));

const LineByLineComplexity = ({ codeInformations }) => {
  const classes = useStyles();

  let expandedAcords = [];
  for (let i = 0; i < codeInformations.length; i++) {
    expandedAcords.push(true);
  }

  const [expanded, setExpanded] = useState(expandedAcords);

  const handleChange = (idx) => (_event, _isExpanded) => {
    let expansions = [...expanded];
    expansions[idx] = !expansions[idx];
    setExpanded(expansions);
  };

  const codeString = `
  import os
  from typing import List
  import argparse
  import json
  
  class Result:
      def __init__(self, accepted: bool, path: str):
          self.accepted = accepted
          self.path = path
  
  def prependNodeToPath(node, path) -> str:
      return node if len(path) is 0 else (node + " -> " + path)`;

  return (
    <div className={classes.root}>
      {codeInformations.map((index, info) => {
        return (
          <Accordion expanded={expanded[index]} onChange={handleChange(index)}>
            <AccordionSummary
              expandIcon={<ExpandMoreIcon />}
              aria-controls="panel1a-content"
              id={`panel-${index}-header`}
            >
              <Typography
                className={classes.heading}
              >{`Section ${index}`}</Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography>
                <SyntaxHighlighter language="python" style={darcula}>
                  {codeString}
                </SyntaxHighlighter>
              </Typography>
            </AccordionDetails>
          </Accordion>
        );
      })}
    </div>
  );
};

export default LineByLineComplexity;

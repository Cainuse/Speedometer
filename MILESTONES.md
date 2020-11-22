# Contents

* [Milestone 4](https://github.students.cs.ubc.ca/cpsc410-2020w-t1/cpsc410_project2_team4/blob/master/MILESTONES.md#milestone-4)
* [Milestone 3](https://github.students.cs.ubc.ca/cpsc410-2020w-t1/cpsc410_project2_team4/blob/master/MILESTONES.md#milestone-3)
* [Milestone 2](https://github.students.cs.ubc.ca/cpsc410-2020w-t1/cpsc410_project2_team4/blob/master/MILESTONES.md#milestone-2)
* [Milestone 1](https://github.students.cs.ubc.ca/cpsc410-2020w-t1/cpsc410_project2_team4/blob/master/MILESTONES.md#milestone-1)

# Milestone 4

## Status of implementation

Completed tasks:

* Line-by-line analysis:
    * Prototyping with Scalene for memory and CPU time profiling
    * Initial implementation of profiler with Scalene (in review)
* End-to-end analysis:
    * Code for creating Dockerfiles for running test program with each sample size (in review)
    * Code for building Docker images from Dockerfiles (in review)
* Visualization
    * Skeleton React app with some graphs using dummy data
    
Tasks to Complete:

* Line-by-line analysis:
    * Debug and integrate with E2E analysis in proper JSON output format to send to front end
* End-to-end analysis:
    * Write code for spinning-up docker containers and measuring stats

## Plans for final user study

- Provide finished implementation of app with instructions to do certain tasks and receive feedback
   - Create test Python files that users can use our tool to analyze to compare expected and actual results
   - Complete front end dashboard for users to provide feedback on
   - Recruit users with Linux/MacOS to help with testing

## Planned timeline for the remaining days

25th Nov - finish implementation (continue fixing bugs and testing)

26th Nov - final user study

27th Nov - start working on video

# Milestone 3

## Mockup of analysis design, including any visualisation planned

Mockup available on Figma [here](https://www.figma.com/file/4YQEQzz0XZD33ePeqh8TxW/FML-Complexity-2.0?node-id=0%3A1)

## Notes about first user studies

See detailed feedback under [docs](docs/).

Summary of feedback:

* Timeline view is good, but descriptions are not very useful
* Line by line analysis is nice but more details would be better
* Performance summary is nice - especially the colour coding
    * Would be nice to plot the actual code runtime on the graph
* For memory usage, would be nice to see which data structures use most memory


## Any changes to original analysis/visualisation design

- Clarified visualization titles, chart legends and run-time specific data percentages for better understanding of dashboard
- Gave timeline more clear descriptions for the entire performance analysis process
- Provided helpful descriptions for each visualization in order to understand the purpose and usefulness of each of them

Aside note:

A lot of the template images for the rough design was taken off online resources that have aspects that may be irrelevant for our purposes even though they are shown as part of the initial design, they will be modified during the actual implementation. This led to receiving feedback on parts we were already aware of that were seemingly incoherent, even though they were simply put in the initial drafted design for completion purposes.

# Milestone 2

## Planned division of main responsibilities between team members

Sketch - as a group
1st prototype user study - individual
implementation - divide by components
2nd prototype user study - individual
video - divide tasks

## Roadmap for what should be done when

6th Nov:

       - Sketch for prototype (sample input/output + wireframe for visualization, med-high fidelity)
       - Describe the stages of analysis (from user's perspective)
       
9th Nov:

       - User study on prototype
20 days:

       - Implement everything
10th Nov:

    precursor: define APIs that connect these components...
12th Nov:

    - Front-end template
    - Docker analysis
    - cProfile analysis
    - Connector (combines data + template)

26th Nov:
       
       - Final user study
27th Nov:

       - Create video
30th Nov:

       - Submit project


## Summary of progress so far

* Identified and expanded on idea
* Breakdown of tasks

# Milestone 1

## Update: Revised project idea after discussions with TA

**Idea Overview:** Dynamic analysis of a Python program to empirically calculate its time/space complexity, as well as provide a module-by-module breakdown of CPU time usage and memory usage.

**Analysis Components:** 

There are 2 parts here...
 
1.Calculation of avg. (wall clock) time  and memory usage by the entire program for different input sizes

This part we will be building ourselves. We will use Docker containers to run the program and monitor the time and memory usage of the container for various input sizes.

2. Calculation of CPU time and memory usage by class/function/line of the Python program

For this part, we'll be using the cProfile library in Python

**Visualization:** 

Our analysis tool will generate a webpage that visualizes the collected data as follows:

1. A line chart that shows the monitored wall clock time for running the program with various input sizes, compared to standard time complexities such as n, nlogn, n^2 ...
2. A line chart that shows the monitored memory usage for running the program with various input sizes, compared to standard memory complexities such as n, nlogn, n^2 ... 
3. A sankey diagram that illustrates how the memory and time usage breaks down from the whole program into various classes/functions
4. A formatted version of the program that was analyzed with each line/function/class annotated with details on how much memory/time it used. Highlights parts of the program that took the most time.


## Ideas for Project 2

### Smart Repo

An analytics dashboard app which gives insights of public github codebases and can suggest improvements based on best practices:

- Static code analysis:
    - Anti-patterns
    - Redundant code
    - linter or code format consistency validation

- Avg size of PR/commits and frequency
- Number of issues
- Pull request analysis such as success rate, failure rate and frequency

Possible tech stack:
ReactJs, NodeJs: Single page web app

Useful React data visualization framework: https://nivo.rocks/


This app would be like a single web page which has a search bar that takes the URL to any public Github repo (could narrow it to a specific language) as input, and then generates a full dashboard filled with charts, graphs and other types of visual analysis that displays to the user any code anti-patterns, inconsistent code formatting or redundant code, as well as some other data about the commit sizes and pull requests history.

### Space Time Complexity

A dynamic analysis tool that emprically calculates the space/time complexity of a piece of code.

For example, if we have a method like this:

```java
public static foo(Integer n, Integer m) {
    .. do something
}
```

The user can build 'test cases' using the `@Complexity` annotation:

```java
@Complexity(n=1)
public test1() {
    foo(1, 1000);  // run foo() with sample size 1
}

@Complexity(n=10)
public test10() {
    foo(10, 1000);  // run foo() with sample size 10
}

@Complexity(n=10)
public test100() {
    foo(100, 1000);  // run foo() with sample size 100
}
```
The tool would then run each of these test cases multiple times to get an average execution time and memory usage. This data would then be plotted on a chart alongside other standard time complexities.

## Feedback from TA

* Both ideas have potential to be a good project
* No major issues
* Avoid simply combining a visualization framework with an analysis framework
* Needs to seek clarification on part of assignment description - will follow up

## Changes based on feedback

* No changes required so far

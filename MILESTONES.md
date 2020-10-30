# Milestone 1

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

## Changes based on feedback
-

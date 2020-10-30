# Milestone 1

## Ideas for Project 2

### Smart Repo

// TODO: Abid can you add a description here?

- Avg size of PR/commits
- Number of issues 

- Anti-patterns
- Redundant code


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
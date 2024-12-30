# Contributing to EpicChain Viper 🌐🚀

Thank you for considering contributing to **EpicChain Viper**! 🎉 We're an open-source project designed to empower blockchain developers by providing a Python-like experience that compiles Python3 code into **EpicChain blockchain-compatible bytecode**. Whether you're a blockchain enthusiast, a Python developer, or just curious about how things work, we welcome your contributions!

To dive deeper into the workings of our project, explore the following sections:  
- [**Product Strategy**](#product-strategy)  
- [**Project Structure**](#project-structure)  

Let's take this journey of blockchain development together. 🌍💻

---

## Product Strategy 🧠🎯

### Pure Python: A Developer-Friendly Approach

We aim to make **EpicChain Viper** feel as close to regular Python as possible for developers. If you’re familiar with Python, you’ll find our approach intuitive and straightforward. We've worked hard to ensure that there are **no new keywords**, instead opting to use **decorators** and **helper functions** for added functionality. This approach ensures that **Python developers** feel right at home when they try **EpicChain Viper** for the first time.

### EpicChain Python Framework: A Comprehensive Toolset

Building a smart contract isn’t just about writing code—developers need a comprehensive environment to **debug**, **deploy**, and **invoke** their contracts. Therefore, **EpicChain Viper** isn't just a standalone tool. It's a crucial part of a larger **Python framework** designed to make your development experience as smooth as possible. This means **logs**, **detailed error messages**, and **informative debugging** tools are integrated to help you build with confidence.

### Testing with EpicChain VM: Trust But Verify ✅

Ensuring that your code works as expected is essential. That's why **EpicChain Viper** integrates testing directly with the **official EpicChain 3 VM**. The **EpicChain Test Runner**, which was originally built for **C# dApp developers**, has been extended for use with Python-based smart contracts. This guarantees that your compiled contracts are tested and functional before deployment, giving you peace of mind.

### Maintenance: Making Life Easy for Developers 🛠️

Building something **maintainable** and **upgradable** is at the heart of **EpicChain Viper**. To keep the codebase clean and easy to evolve, we focus on writing **unit tests**, **documented code**, and ensuring that every feature is **typed correctly**. This ensures that **EpicChain Viper** remains reliable and adaptable for future changes.

### Releases: Keeping the Progress Flowing 📦

When a set of issues is resolved, a new release branch is created, and those issues are cherry-picked into the branch. Using the **[bump-my-version](https://github.com/callowayproject/bump-my-version)** tool, we increment the version number, update the changelog, and publish the new version. After rigorous testing on **CircleCI**, the release is approved and pushed to **PyPi**. Documentation updates are also published alongside each new release, ensuring you always have the latest info at your fingertips.

---

## Project Structure 📂🛠️

The **EpicChain Viper** project is structured in a modular way to keep things clean and manageable. Below is a high-level overview of the core components that make up the project.

<p align="center">
  <img src="/.github/resources/images/diagram.png" width="500px" alt="EpicChain Viper Project Structure">
</p>

Each folder in the project serves a specific purpose, and understanding the organization will make it easier for you to contribute. Let's break it down:

---

## New Features or Issues 💡🐞

Found a bug or have a great feature idea? Awesome! We welcome contributions and encourage you to check the [**Issues Page**](https://github.com/CityOfZion/EpicChainViper/issues) to see if your issue has already been reported. If not, don’t hesitate to [create a new issue](https://github.com/CityOfZion/EpicChainViper/issues/new/choose).

### When submitting an issue, please:
- **Keep the title concise** and descriptive.
- **Provide context**, such as a code snippet where the problem occurred or an example of the missing feature.
- **Describe the expected behavior** clearly so that we know how the feature or fix should function.

---

## Setting Up Your Workspace 🖥️🔧

To contribute to **EpicChain Viper**, you’ll need a **Python3 version 3.11 or higher** and a few other tools. Follow these steps to get your environment set up and ready for development:

1. Install the necessary Python packages:

    ```bash
    pip install -e .[dev,test]
    ```

2. Install **EpicChain.Express** and **EpicChain.Test.Runner** via dotnet:

    ```bash
    dotnet tool install EpicChain.Express --version 3.5.20 -g
    dotnet tool install EpicChain.Test.Runner --version 3.5.17 -g
    ```

> **Note:** Some tests may fail if **EpicChain Viper** is installed as a package, as we only need the dependencies. Therefore, it is being uninstalled.

---

## Writing Code: Organizing Your Changes 📝

**EpicChain Viper** is divided into three main directories:

- **`boa3/builtin`**: Contains interfaces for the methods available to be called in contracts.
- **`boa3/internal`**: The heart of the project, this folder holds the actual method implementations, classes, and types. It also handles script validation during compilation.
    - **`boa3/internal/analyser`**: Optimizes and analyzes scripts.
    - **`boa3/internal/model`**: Contains the implementation of methods and types.
- **`boa3_test`**: Contains unit tests to ensure everything works as expected.

When adding new features, you’ll likely need to modify files within both **`boa3/builtin`** and **`boa3/internal`**. If you’re adding a Python feature missing from **EpicChain Viper**, you’ll only need to work within **`boa3/internal`**.

> **Tip:** Follow **PEP8** for clean and consistent code. You can use **autopep8** to format your code automatically. We recommend using the flags `autopep8 -r -i -a -a .`, but be cautious as some imports cannot be auto-fixed due to circular import issues.

### Testing: Ensuring Quality 🧪

We take testing seriously. Every new feature or bug fix should come with **unit tests**. Use **CircleCI**, **EpicChain Test Runner**, and **EpicChain-Express** to run tests. To run all tests, execute the Python script:

```bash
python boa3_test/tests/run_unit_tests.py
```

This ensures that all tests pass before changes are merged.

---

## Submitting Pull Requests: Sharing Your Work 🤝

Once you’ve implemented a new feature or fixed a bug, it's time to submit a **Pull Request**. While we don’t have a strict naming convention for branches or commits, please ensure your descriptions are clear and informative. This will help us understand the changes you’ve made.

We also have a **Pull Request template** to guide you in detailing your changes. You don’t need to fill in every section, but the more context you provide, the easier it will be for us to review and merge your contribution.

---

**Together, we can make EpicChain Viper the go-to tool for blockchain developers!** 🌟 Happy coding!
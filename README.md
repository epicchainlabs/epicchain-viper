<p align="center" style="font-size: 1.5rem; font-weight: bold; color: #2c3e50;">
  Revolutionize Blockchain Development: Write Smart Contracts for <span style="color: #e74c3c;">EpicChain</span> in Python
  <br/>
  Brought to You by <b style="color: #3498db;">EpicChain Lab's</b>
</p>

<p align="center" style="font-size: 1.2rem;">
  <a href="https://github.com/epicchainlabs/epicchain-viper" style="color: #1abc9c; text-decoration: none;"><strong>epicchain-viper</strong></a> · 
  <a href="https://github.com/epicchainlabs/epicchain-raptor" style="color: #9b59b6; text-decoration: none;">epicchain-raptor</a> · 
  <a href="https://github.com/epicchainlabs/cpm" style="color: #e67e22; text-decoration: none;">cpm</a>
</p>

<hr style="border: 1px solid #bdc3c7; margin: 20px auto; width: 80%;">

<blockquote style="font-size: 1rem; color: #7f8c8d;">
  <b>Note:</b> The latest release (<code>v0.14.0</code>) introduces breaking changes for contracts written with earlier versions. Please refer to our <a href="/docs/migration-guide-v0.14.0.md" style="color: #3498db;">Migration Guide</a> to seamlessly update your smart contracts.
</blockquote>

<h2 style="font-size: 1.8rem; color: #34495e; margin-top: 30px;">Table of Contents</h2>
<ul style="font-size: 1.2rem; line-height: 1.6; color: #2c3e50;">
  <li><a href="#overview" style="color: #e67e22; text-decoration: none;">Overview</a></li>
  <li><a href="#quickstart" style="color: #9b59b6; text-decoration: none;">Quickstart</a>
    <ul>
      <li><a href="#installation" style="color: #1abc9c; text-decoration: none;">Installation</a></li>
      <ul>
        <li><a href="#pip-recommended" style="color: #3498db; text-decoration: none;">Pip (Recommended)</a></li>
        <li><a href="#build-from-source-optional" style="color: #34495e; text-decoration: none;">Build from Source (Optional)</a></li>
      </ul>
    </ul>
  </li>
  <li><a href="#docs" style="color: #e74c3c; text-decoration: none;">Docs</a></li>
  <li><a href="#reference-examples" style="color: #3498db; text-decoration: none;">Reference Examples</a></li>
  <li><a href="#contributing" style="color: #9b59b6; text-decoration: none;">Contributing</a></li>
  <li><a href="#license" style="color: #1abc9c; text-decoration: none;">License</a></li>
</ul>

<h2 id="overview" style="font-size: 1.8rem; color: #34495e;">Overview</h2>
<p style="font-size: 1.2rem; line-height: 1.6; color: #2c3e50;">
  <b>EpicChain Viper</b> is a powerful tool for creating Smart Contracts on the EpicChain blockchain using Python. This compiler transforms your <code>.py</code> files into <code>.nef</code> and <code>.manifest.json</code> formats for execution on the EpicChain Virtual Machine.
</p>
<p style="font-size: 1.2rem; line-height: 1.6; color: #2c3e50;">
  It is part of the <b>EpicChain Python Framework</b>, a comprehensive suite enabling developers to build decentralized applications (dApps) using Python alone.
</p>

<h2 id="quickstart" style="font-size: 1.8rem; color: #34495e;">Quickstart</h2>
<p style="font-size: 1.2rem; line-height: 1.6; color: #2c3e50;">
  Before you begin, ensure you have <b>Python 3.10</b> or later installed on your system.
</p>

<h3 id="installation" style="font-size: 1.6rem; color: #e67e22;">Installation</h3>

<h4 style="font-size: 1.4rem; color: #34495e;">Step 1: Set Up a Virtual Environment</h4>
<p style="font-size: 1.2rem; line-height: 1.6; color: #2c3e50;">
  Create and activate a Python virtual environment:
</p>

<div style="background: #ecf0f1; padding: 15px; border-radius: 5px;">
<b>Linux / Mac OS:</b>
<pre style="font-size: 1.1rem; line-height: 1.6;">
$ python3 -m venv venv
$ source venv/bin/activate
</pre>
<b>Windows:</b>
<pre style="font-size: 1.1rem; line-height: 1.6;">
$ python3 -m venv venv
$ venv\Scripts\activate.bat
</pre>
</div>

<h4 id="pip-recommended" style="font-size: 1.4rem; color: #1abc9c;">Step 2: Pip Installation (Recommended)</h4>
<p style="font-size: 1.2rem; line-height: 1.6; color: #2c3e50;">
  Install <b>EpicChain Viper</b> with pip:
</p>
<pre style="background: #ecf0f1; padding: 15px; border-radius: 5px; font-size: 1.1rem;">
$ pip install epicchain-viper
</pre>

<h4 id="build-from-source-optional" style="font-size: 1.4rem; color: #34495e;">Step 3: Build from Source (Optional)</h4>
<p style="font-size: 1.2rem; line-height: 1.6; color: #2c3e50;">
  If pip is unavailable, you can run EpicChain Viper directly from its source:
</p>
<pre style="background: #ecf0f1; padding: 15px; border-radius: 5px; font-size: 1.1rem;">
$ git clone https://github.com/epicchainlabs/epicchain-viper.git
$ pip install wheel
$ pip install -e .
</pre>

<h2 id="reference-examples" style="font-size: 1.8rem; color: #34495e;">Reference Examples</h2>
<p style="font-size: 1.2rem; line-height: 1.6; color: #2c3e50;">
  Explore comprehensive examples:
  <ul>
    <li><a href="/epicchain_test/examples" style="color: #e74c3c; text-decoration: none;">Smart Contract Examples</a></li>
    <li><a href="/epicchain_test/test_sc" style="color: #1abc9c; text-decoration: none;">Feature Tests</a></li>
  </ul>
</p>

<h2 id="contributing" style="font-size: 1.8rem; color: #34495e;">Contributing</h2>
<p style="font-size: 1.2rem; line-height: 1.6; color: #2c3e50;">
  Join our community of contributors by checking out our <a href="CONTRIBUTING.md" style="color: #9b59b6;">Contributing Guide</a>. Your input drives innovation!
</p>

<h2 id="license" style="font-size: 1.8rem; color: #34495e;">License</h2>
<p style="font-size: 1.2rem; line-height: 1.6; color: #2c3e50;">
  This project is open-source and available under the <a href="https://github.com/epicchainlabs/epicchain-viper/blob/master/LICENSE" style="color: #e67e22;">Apache 2.0 License</a>.
</p>

# Principles of Web Crawler

## 1. Definition
A **web crawler**, sometimes called a **spider**, is an Internet bot that systematically browses the World Wide Web, typically for the purpose of web indexing or web spidering.

## 2. Architecture

![Architecture of a web crawler](https://upload.wikimedia.org/wikipedia/commons/d/df/WebCrawlerArchitecture.svg)

## 3. Procedures
1. Start with a list of URLs to visit, called *__seeds__*.
2. Identify all the hyperlinks in the page and adds them to the list of URLs to visit, called *__crawl frontier__*.
3. Visit recursively the URLs from the frontier according to a set of policies.
4. Copy and save the information if performing archiving of websites.

## 4. Crawling Policies
1. **Selection policy**: states the pages to download
2. **Re-visit policy**: states when to check for changes to the pages
3. **Politeness policy**: states how to avoid overloading websites
4. **Parallelization policy**: states how to coordinate distributed web crawlers

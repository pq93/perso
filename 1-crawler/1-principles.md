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

## 5. Framework of Scrapy

![Framework of Scrapy](https://pic2.zhimg.com/80/v2-f9a34c578b7193f5772c26891d283c55_hd.jpg)

1. **Spiders**: Parse web content, generate scraped objects and additional requests. It's the core of the project, which need to be implemented manually. (= getContent)
2. **Item pipelines**: Write the scraped data into text or database. It's the process of localization, which need to be implemented manually.
3. **Downloader**: Get web content. Prepared by Scrapy. (= getHtml)
4. **Scheduler**: Manage all the requests with multi-thread and concurrent processing. Prepared by Scrapy.
5. **Engine**: Control all the data flow exchange of all the modules, send correspondent event in different conditions.. It's the center of the framework and prepared by Scrapy too.

![Dataflow](https://pic1.zhimg.com/80/v2-a882bb4ccab048a930252e272ff9da1d_hd.jpg)
#### Data flow of Scrapy:
1. **Engine** gets a request from **Spider**.
2. **Engine** transfers the request to **Scheduler**.
3. **Engine** gets next request to be executed from **Scheduler**.
4. **Engine** sends the request to **Downloader** via **Middleware**.
5. After the web crawling, **Engine** gets a response from **Downloader**.
6. **Engine** returns the response to **Spider**.
7. **Spider** handles the response and returns scraped objects and a new request to **Engine**.
8. **Engine** sends the scraped objects to **Item pipeline** (write to database).
9. Next round: **Engine** transfers the request to **Scheduler**.

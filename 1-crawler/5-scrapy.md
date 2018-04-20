## Framework of Scrapy

![Framework of Scrapy](https://pic2.zhimg.com/80/v2-f9a34c578b7193f5772c26891d283c55_hd.jpg)

1. **Spiders**: Parse web content, generate grabbed objects and additional requests. It's the core of the project, which need to be implemented manually. (= getContent)
2. **Item pipelines**: Write the grabbed data into text or database. It's the process of localization, which need to be implemented manually.
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
7. **Spider** handles the response and returns grabbed objects and a new request to **Engine**.
8. **Engine** sends the grabbed objects to **Item pipeline** (write to database).
9. Next round: **Engine** transfers the request to **Scheduler**.

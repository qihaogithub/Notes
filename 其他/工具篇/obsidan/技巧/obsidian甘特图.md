#软件/obsidian  #插件
```mermaid
gantt
    title 这里是标题
    axisFormat %m-%d
    dateFormat  YYYY-MM-DD
    excludes    weekends
    todayMarker stroke-width:5px,stroke:#0f0,opacity:0.5

    section 常规任务
	已完成任务           :done,    20220906, 2022-09-06,2022-09-08
	click 20220906 href "obsidian://open?vault=%E6%88%91%E7%9A%84%E7%AC%94%E8%AE%B0&file=2%C2%B7%E7%AC%94%E8%AE%B0%2F%E5%85%B6%E4%BB%96%2Fobsidian%2F%E5%88%86%E6%A0%8F%E6%8F%92%E4%BB%B6"  
	
    进行中任务           :active,  des2, 2022-09-08, 3d
    未来任务             :         des3, after des2, 5d

	click des2 call printArguments("test1", "test2", test3) 
	click des3 call printTask()

	section 关键任务
    已完成关键任务      :crit, done, 2022-09-18,24h
    已完成关键任务      :crit, done, after des1, 2d
    进行中关键任务       :crit, active, 3d
    未来关键任务       :crit, 5d
    任务       :2d
    任务          :1d
    标点            :milestone, 2022-09-19, 0d
    
    section 文档
    描述甘特语法              :active, a1, after des1, 3d
    将甘特图添加到演示页面      :after a1  , 20h
    将另一个图表添加到演示页面   :doc1, after a1  , 48h
    
    section 最后一节
    描述甘特语法              :after doc1, 3d
    将甘特图添加到演示页面      :20h
    将另一个图表添加到演示页面   :48h

 
```



excludes    weekends 
> 排除周末
> 接受  "YYYY-MM-DD"  "sunday"  "weekends"

todayMarker stroke-width:5px,stroke:#0f0,opacity:0.5
> 今天标记
> 若要隐藏，写“todayMarker off”

click 任务ID href "ob链接"  
> 给任务添加点击时间
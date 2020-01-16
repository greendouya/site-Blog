# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "https://blog.wooocloud.com/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "greendouya/site-Blog@gh-pages"
}
category_by_folder = True
for_manual_build_trigger = 2

# 站点设置
site_name = "稳妥国字脸"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2020-01-15 16:30"
author = "Dragon"
email = "gotspinach@foxmail.com"
author_homepage = "http://blog.wooocloud.com"
description = "7.24也算个节日了么?"
key_words = ['Linux', 'Docker', 'ELK', '运维']
language = 'zh-CN'
external_links = [
    {
        "name": "成人交友",
        "url": "https://github.com/greendouya",
        "brief": "Go?go...Go!"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    # {
    #     "name": "友链",
    #     "url": "${site_prefix}links/",
    #     "target": "_self"
    # },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/greendouya",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "",
        "icon": "gi gi-weibo"
    }
]

# valine = {
#     "enable": True,
#     "el": '#vcomments',
#     "appId": "6chFXPTjrjYnjFk9duROcboN-gzGzoHsz",
#     "appKey": "c1CRooaFmpLs4xi7x3YLm3ma",
#     "visitor": True,
#     "recordIP": True,
#     "placeholder": "来畅所欲言吧~"
# }

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//blog.imalan.cn" />
<!--
<link rel="stylesheet" href="${static_prefix}brand_font/embed.css" />
<style>.brand{font-family:FZCuJinLFW,serif;font-weight: normal!important;}</style>
-->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="apple-touch-icon" sizes="180x180" href="${static_prefix}apple-touch-icon.png?v=PY43YeeEKx">
<link rel="icon" type="image/png" sizes="32x32" href="${static_prefix}favicon-32x32.png?v=yyLyaqbyRG">
<link rel="icon" type="image/png" sizes="16x16" href="${static_prefix}favicon-16x16.png?v=yyLyaqbyRG">
<link rel="mask-icon" href="${static_prefix}safari-pinned-tab.svg?v=yyLyaqbyRG" color="#505050">
<link rel="shortcut icon" href="${static_prefix}favicon.ico?v=yyLyaqbyRG">
<meta name="application-name" content="稳妥国字脸">
<meta name="apple-mobile-web-app-title" content="稳妥国字脸">
<meta name="msapplication-TileColor" content="#000000">
<meta name="theme-color" content="#000000">
<meta name="baidu-site-verification" content="9BEwwo6Ibg" />
'''

footer_addon = r'''
<a no-style href="http://beian.miit.gov.cn" target="_blank"></a>
'''

body_addon = r'''
<script>
    var _hmt = _hmt || [];
    (function() {
    var hm = document.createElement("script");
    hm.src = "https://hm.baidu.com/hm.js?e4f3a7c02ac2aabc41a1cfa95f61a026";
    var s = document.getElementsByTagName("script")[0]; 
    s.parentNode.insertBefore(hm, s);
    })();
</script>
<script>
    (function(){
        var bp = document.createElement('script');
        var curProtocol = window.location.protocol.split(':')[0];
        if (curProtocol === 'https') {
            bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
        }
        else {
            bp.src = 'http://push.zhanzhang.baidu.com/push.js';
        }
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(bp, s);
    })();
</script>
<script>
if(window.location.hash){
    var checkExist = setInterval(function() {
       if ($(window.location.hash).length) {
          $('html, body').animate({scrollTop: $(window.location.hash).offset().top-90}, 1000);
          clearInterval(checkExist);
       }
    }, 100);
}
</script>
<script>
if(window.navigator && navigator.serviceWorker) {
  caches.keys().then(function(cacheNames) {
    cacheNames.forEach(function(cacheName) {
      caches.delete(cacheName);
    });
  }).then(function(){
    console.log('Cache cleaned.');
  });
  navigator.serviceWorker.getRegistrations()
  .then(function(registrations) {
    for(let registration of registrations) {
      registration.unregister();
    }
  }).then(function(){
    console.log('Service Worker stopped.');
  });
}
</script>
'''

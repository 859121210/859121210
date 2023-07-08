#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import time
import base64

class Spider(Spider):  # 元类 默认的元类 type
    def getName(self):
        return "明星MV"
    def init(self,extend=""):
        print("============{0}============".format(extend))
        pass
    def isVideoFormat(self,url):
        pass
    def manualVideoCheck(self):
        pass
    def homeContent(self,filter):
        result = {}
        cateManual = {
          "粤语":"粤语MV4k合集",
    "2022年热榜":"2022年热门MV4k合集",
    "KTV热门":"KTV热门MV4k合集",
    "滚石经典":"滚石MV4k合集",
    "经典老歌":"经典老歌",
    "古风MV":"古风MV4k合集",
    "闽南语MV":"闽南语MV4k合集",
    "印度歌舞":"印度歌舞MV4k合集",

    "网红翻唱":"网红翻唱MV4k合集",
    "韩国女团":"韩国女团MV4k合集",
    "A阿黛尔":"阿黛尔MV4k合集",
    
    "Blackpink":"blackpinkMV4k合集",
    "Beyond":"beyondMV超清合集",
    "B坂井泉水":"坂井泉水MV超清合集",
    "B宝丽金":"宝丽金MV超清合集",
    "B布兰妮":"布兰妮MV超清合集",
    "C崔健":"催件MV超清合集",
    "C草蜢":"草蜢MV超清合集",
    "Coldplay":"coldplayMV超清合集",
    "C陈慧娴":"陈慧娴MV超清合集",
    "C陈百强":"陈百强MV超清合集",
    "C陈淑桦":"陈淑桦MV超清合集",
    "C陈楚生":"陈楚生MV超清合集",
    "C陈慧琳":"陈慧琳MV超清合集",
    "D邓丽君":"邓丽君MV超清合集",
    "D邓紫棋":"邓紫棋MV超清合集",
     "D刀郎":"刀郎MV超清合集",
    "D达明一派":"刘以达MV超清合集",
    "F费玉清":"费玉清MV超清合集",
    "F飞图":"飞图MV超清合集",
    "G谷村新司":"谷村新司MV超清合集",
    "G郭富城":"郭富城MV超清合集",
    "G关淑怡":"关淑怡MV超清合集",
    "H黄凯芹":"黄凯芹MV超清合集",
    "J降央卓玛":"降央卓玛MV超清合集",
    
    "J江慧":"江慧MV超清合集",
    "J吉永小百合":"吉永小百合MV超清合集",
    "J金庸":"金庸影视MV超清合集",
    "K柯以敏":"柯以敏MV超清合集",
    "K邝美云":"邝美云MV超清合集",
    "L刘德华":"刘德华MV超清合集",
    "Lady Gaga":"Lady GagaMV超清合集",
    "L龙飘飘":"龙飘飘MV超清合集",
    "L罗大佑":"罗大佑MV",
    "L林志炫":"林志炫MV",
    "L林忆莲":"林忆莲MV",
    "L李知恩":"李知恩MV",
    "L梁静茹":"梁静茹MV",
    "L冷漠":"冷漠MV",
    "L李克勤":"李克勤MV",
    "L林子祥":"林子祥MV",
    "L黎明":"黎明MV",
    "L刘若英":"刘若英MV",
    "M莫文蔚":"莫文蔚MV",
    "M孟庭苇":"孟庭苇MV",
    "M麦当娜":"麦当娜MV",

    "M迈克杰克逊":"迈克杰克逊MV",
    "N雅尼紫禁城":"雅尼紫禁城MV",
    "P潘越云":"潘越云MV",
    "P潘美辰":"潘美辰MV",
    "Q齐秦":"齐秦MV",
    
    "R任贤齐":"任贤齐MV",
    "S苏慧伦":"苏慧伦MV",
    "T童安格":"童安格MV",
    "TFBOYS":"TFBOYSMV",
    "T太极乐队":"太极乐队MV",
    "T唐朝摇滚":"唐朝摇滚MV",
    
    "T谭咏麟":"谭咏麟MV",
    
    "W王琪":"王琪MV",
     "W伍珂玥":"伍珂玥MV",
    "W王杰":"王杰MV",
    "W伍佰":"伍佰MV",
    "W温兆伦":"温兆伦MV",
    "W王菲":"王菲MV",
    "X徐小凤":"徐小凤MV",
    "X席琳迪翁":"席琳迪翁MV",
    "X许嵩":"黄许嵩MV",
    "X许美静":"许美静MV",
    "X许冠杰":"许冠杰MV",
    "X熊天平":"熊天平MV",
    "X小虎队":"小虎队MV",
    "X许巍":"许巍MV",
    "Y叶启田":"叶启田MV",
    "Y杨钰莹":"杨钰莹MV",
    "Y叶玉卿":"叶玉卿MV",
    "Y杨千嬅":"杨千嬅MV",
    "Y怡正宵":"怡正宵MV",
    "Z左麟右李":"左麟右李MV",
    "Z张楚":"张楚MV",
    "Z张真":"张真MV",
    "Z张震岳":"张震岳MV",
    "Z赵传":"赵传MV",
    "Z周华健":"周华健MV",
    "Z周启生":"周启生MV",
    "Z张信哲":"张信哲MV",
    "Z张也":"张也MV",
    
    "Z周慧敏":"周慧敏MV",
   
    "Z张碧晨":"张碧晨MV",
    "Z中岛美雪":"中岛美雪MV",
    "Z张学友":"张学友MV",
    "Z猪哥亮":"猪哥亮MV",
    "Z周杰伦":"周杰伦MV",
    "Z周深":"周深MV",
    "Z张蔷":"张蔷MV",
    "Z张帝":"张帝MV",
    "Z张国荣":"张国荣MV",
    "Z周传雄":"周传雄MV"
        }
        classes = []
        for k in cateManual:
            classes.append({
                'type_name':k,
                'type_id':cateManual[k]
            })
        result['class'] = classes
        if(filter):
            result['filters'] = self.config['filter']
        return result
    def homeVideoContent(self):
        result = {
            'list':[]
        }
        return result
    cookies = ''
    def getCookie(self):
        import requests
        import http.cookies
        # 这里填cookie
        raw_cookie_line ="buvid3=8B57D3BA-607A-1E85-018A-E8C430023CED42659infoc; b_lsid=BEB8EE7F_18742FF8C2E; bsource=search_baidu; _uuid=DE810E367-B52C-AF6E-A612-EDF4C31567F358591infoc; b_nut=100; buvid_fp=711a632b5c876fa8bbcf668c1efba551; SESSDATA=7624af93%2C1696008331%2C862c8%2A42; bili_jct=141a474ef3ce8cf2fedf384e68f6625d; DedeUserID=3493271303096985; DedeUserID__ckMd5=212a836c164605b7; sid=5h4ruv6o; buvid4=978E9208-13DA-F87A-3DC0-0B8EDF46E80434329-123040301-dWliG5BMrUb70r3g583u7w%3D%3D"
        simple_cookie = http.cookies.SimpleCookie(raw_cookie_line)
        cookie_jar = requests.cookies.RequestsCookieJar()
        cookie_jar.update(simple_cookie)
        return cookie_jar
    def get_dynamic(self,pg):
        result = {}
        
        url= 'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=all&page={0}'.format(pg)
        
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['items']
            for vod in vodList:
                if vod['type'] == 'DYNAMIC_TYPE_AV':
                    ivod = vod['modules']['module_dynamic']['major']['archive']
                    aid = str(ivod['aid']).strip()
                    title = ivod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
                    img =  ivod['cover'].strip()
                    remark = str(ivod['duration_text']).strip()
                    videos.append({
                        "vod_id":aid,
                        "vod_name":title,
                        "vod_pic":img,
                        "vod_remarks":remark
                    })
                result['list'] = videos
                result['page'] = pg
                result['pagecount'] = 9999
                result['limit'] = 90
                result['total'] = 999999
        return result

    def get_hot(self,pg):
        result = {}
        url= 'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={0}'.format(pg)
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
                img =  vod['pic'].strip()
                remark = str(vod['duration']).strip()
                videos.append({
                    "vod_id":aid,
                    "vod_name":title,
                    "vod_pic":img,
                    "vod_remarks":remark
                })
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = 9999
            result['limit'] = 90
            result['total'] = 999999
        return result
    def get_rank(self):
        result = {}
        url= 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
                img =  vod['pic'].strip()
                remark = str(vod['duration']).strip()
                videos.append({
                    "vod_id":aid,
                    "vod_name":title,
                    "vod_pic":img,
                    "vod_remarks":remark
                })
            result['list'] = videos
            result['page'] = 1
            result['pagecount'] = 1
            result['limit'] = 90
            result['total'] = 999999
        return result
    def categoryContent(self,tid,pg,filter,extend):	
        result = {}
        if tid == "热门":
            return self.get_hot(pg=pg)
        if tid == "排行榜" :
            return self.get_rank()
        if tid == '动态':
            return self.get_dynamic(pg=pg)
        url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword={0}&page={1}'.format(tid,pg)
        if len(self.cookies) <= 0:
            self.getCookie()
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] != 0:			
            rspRetry = self.fetch(url,cookies=self.getCookie())
            content = rspRetry.text		
        jo = json.loads(content)
        videos = []
        vodList = jo['data']['result']
        for vod in vodList:
            aid = str(vod['aid']).strip()
            title = tid + ":" + vod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
            img = 'https:' + vod['pic'].strip()
            remark = str(vod['duration']).strip()
            videos.append({
                "vod_id":aid,
                "vod_name":title,
                "vod_pic":img,
                "vod_remarks":remark
            })
        result['list'] = videos
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result
    def cleanSpace(self,str):
        return str.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    def detailContent(self,array):
        aid = array[0]
        url = "https://api.bilibili.com/x/web-interface/view?aid={0}".format(aid)

        rsp = self.fetch(url,headers=self.header,cookies=self.getCookie())
        jRoot = json.loads(rsp.text)
        jo = jRoot['data']
        title = jo['title'].replace("<em class=\"keyword\">","").replace("</em>","")
        pic = jo['pic']
        desc = jo['desc']
        typeName = jo['tname']
        vod = {
            "vod_id":aid,
            "vod_name":title,
            "vod_pic":pic,
            "type_name":typeName,
            "vod_year":"",
            "vod_area":"bilidanmu",
            "vod_remarks":"",
            "vod_actor":jo['owner']['name'],
            "vod_director":jo['owner']['name'],
            "vod_content":desc
        }
        ja = jo['pages']
        playUrl = ''
        for tmpJo in ja:
            cid = tmpJo['cid']
            part = tmpJo['part']
            playUrl = playUrl + '{0}${1}_{2}#'.format(part,aid,cid)

        vod['vod_play_from'] = '🌸荷城茶秀接口🌸B站线路'
        vod['vod_play_url'] = playUrl

        result = {
            'list':[
                vod
            ]
        }
        return result
    def searchContent(self,key,quick):
        search = self.categoryContent(tid=key,pg=1,filter=None,extend=None)
        result = {
            'list':search['list']
        }
        return result
    def playerContent(self,flag,id,vipFlags):
        # https://www.555dianying.cc/vodplay/static/js/playerconfig.js
        result = {}

        ids = id.split("_")
        url = 'https://api.bilibili.com:443/x/player/playurl?avid={0}&cid=%20%20{1}&qn=112'.format(ids[0],ids[1])
        rsp = self.fetch(url,cookies=self.getCookie())
        jRoot = json.loads(rsp.text)
        jo = jRoot['data']
        ja = jo['durl']
        
        maxSize = -1
        position = -1
        for i in range(len(ja)):
            tmpJo = ja[i]
            if maxSize < int(tmpJo['size']):
                maxSize = int(tmpJo['size'])
                position = i

        url = ''
        if len(ja) > 0:
            if position == -1:
                position = 0
            url = ja[position]['url']

        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = url
        result["header"] = {
            "Referer":"https://www.bilibili.com",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        result["contentType"] = 'video/x-flv'
        return result

    config = {
        "player": {},
        "filter": {}
    }
    header = {}

    def localProxy(self,param):
        return [200, "video/MP2T", action, ""]

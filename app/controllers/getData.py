# encoding=UTF-8
from pyquery import PyQuery as pyq
from app.module.statusCode import get_statusCode
import re
import json
import os


def getData(resHtml):  # 从html中获取数据
    try:
        resHtml.encoding = 'utf-8'
        jq = pyq(resHtml.text)

        # print(jq('meta[property="og:image"]').attr("content"))

        fileImg = jq('meta[property="og:image"]').attr("content")
        srclist = jq('script')

        profilePicture = ""
        profileName = ""
        title = ""

        for src in range(int(len(srclist))):
            # print(jq('script').eq(src).html())
            html = jq('script').eq(src).html()
            try:
                top = re.search('{(.*)}', html)
                if top != None:
                    loadData = json.loads(top.group())
                    profilePicture = loadData["entry_data"]["PostPage"][0][
                        "graphql"]["shortcode_media"]["owner"]["profile_pic_url"]
                    profileName = loadData["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["username"]
                    title = loadData["entry_data"]["PostPage"][0]["graphql"][
                        "shortcode_media"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
            except Exception as e:
                print(e, src)

        res = get_statusCode("2000")
        res["data"] = {
            "fileImg": fileImg,
            "profilePicture": profilePicture,
            "profileName": profileName,
            "title": title,
        }
        return res
    except Exception as e:
        res = get_statusCode("4003")
        res["error"] = e
        return res

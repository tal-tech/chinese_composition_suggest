# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')
import pycorrector


# 那天花板上的钻石可比鸡弹（（蛋））还大啊。
# 才般（（搬））进装修好没多久的新宫殿里。
# 做的最倒霉的一件事就帮尼哥檫（（擦））脚。
# 一但（（旦））死去，以前花费的心血都会归零。
# 战士微笑著（（着））轻轻拍了拍少年的肩膀。
# 差点拌（（绊））到自己的脚。
# 面对着熙熙嚷嚷（（攘攘））的城市。
# 你等我和老大商却（（榷））一下。
# 这家伙还蛮格（（恪））尽职守的。
# 玩家取明（（名））“什么”已被占用。
# 报应接中迩（（而））来。
# 人群穿（（川））流不息。
# 这个消息不径（（胫））而走。
# 眼前的场景美仑（（轮））美幻简直超出了人类的想象。
# 看着这两个人谈笑风声（（生））我心理（（里））不由有些忌妒。
# 有老怪坐阵（（镇））难怪他们高枕无忧了。
# 有了这一番旁证（（征））博引。


def test_char_correct_right():
    errors = [
        '少先队员因该为老人让坐',
        '服装店里的衣服各试各样',
        '那天花板上的钻石可比鸡弹还大啊',
        '才般进装修好没多久的新宫殿里。',
        '一但死去，以前花费的心血都会归零。',
        '这家伙还蛮格尽职守的。',
        '玩家取明“什么”已被占用。',
        '人群穿流不息。',
        '这个消息不径而走。',
        '眼前的场景美仑美幻简直超出了人类的想象。',
        '看着这两个人谈笑风声',
        '有老怪坐阵难怪他们高枕无忧了。',
        '有了这一番旁证博引。',
    ]
    for i in errors:
        print(i, pycorrector.correct(i))


def test_char_correct_wrong():
    errors = [
        '她知难而上，沤心沥血，一心扑在舞台上',
        '还有你们看看清除哈',
        '我国人民义愤填鹰',
        '权利的游戏第八季',
        '2周岁22斤宝宝用多大的啊',
        '这个到底有多辣?',
        '所以先救挨饿的人，然后治疗病人。',
        '现在，常常会到听男女平等这个词。',
        '我的喉咙发炎了要买点阿莫细林吃',
        '做的最倒霉的一件事就帮尼哥檫脚。',
        '战士微笑著轻轻拍了拍少年的肩膀。',
        '差点拌到自己的脚。',
        '面对着熙熙嚷嚷的城市。',
        '你等我和老大商却一下。',
        '报应接中迩来。',
        '我心理不由有些忌妒。',
        '他们不需要怕他门没有钱。',
        '全球的产龄妇女总生育率只生下一半，根据调查很有可能一直到2050年产龄妇女总生育率还是减少的趋势。',
        '但现代的妇女所担任的责任已家重，除了家务以外，仍需出外工作补贴家',
        '加上父母亲自己的看法，想原封不动地、完完全全地全部传给子女们',
        '叶子的绿色与本身枝干的颜色都会变为偏较暗的颜色。',
    ]
    for i in errors:
        print(i, pycorrector.detect(i))
        print(i, pycorrector.correct(i))

# coding: utf-8
import unittest
import time
import askfm.parser
import six

class ParserTest(unittest.TestCase):
    def test_parse_question(self):
        html = u'''
<div class="item streamItem streamItem-answer">
    <div class="streamItemContent streamItemContent-question">
      <h2>おいC++エヴァンゲリオン、C++ではなくSwiftを選ぶGoogleを許していいのか？</h2>
</div>
  <p class="streamItemContent streamItemContent-answer_old">Swiftは<br />罠がありそうで怖い。</p>
  <div class="streamItemContent streamItemContent-footer">
    <a class="streamItemsAge" title="5月 13, 2016 14:11:43 GMT" href="/EzoeRyou/answers/135859194711">5ヵ月前</a>
</div>
  <div class="streamItemOptions afm-popover-container">
    <div class="likeButton">
    <a class="icon-like" title="いいね！" data-action="AnswerLikeToggle" data-url="/EzoeRyou/answers/135859194711/likes" data-gtm="like-toggle" href="#"></a>
  <a class="counter" style="display:none" href="/EzoeRyou/answers/135859194711">0</a>
</div>
    <a title="その他" class="streamItemOptions-more icon-more" data-action="PopoverOpen" href="#"></a><nav class="afm-popover right" style="display:none"><a class="icon-flag" data-action="PopupOpen" data-url="/EzoeRyou/answers/135859194711/flag" data-gtm="{&quot;name&quot;:&quot;popup&quot;,&quot;meta&quot;:[&quot;report-topic&quot;,&quot;Answer reports&quot;,&quot;New reason&quot;]}" href="#">投稿の報告</a><a class="icon-block" data-action="PopupOpen" data-url="/EzoeRyou/flag/block" data-gtm="{&quot;name&quot;:&quot;popup&quot;,&quot;meta&quot;:[&quot;report-topic&quot;,&quot;Answer reports&quot;,&quot;New block&quot;]}" href="#">ユーザーのブロック</a></nav>
    <a class="rsp-lte-tablet streamItemOptions-reask icon-reask" data-action="ButtonPostOnce" data-url="/account/ask-friends" data-method="put" data-title="再度質問する" data-params="{&quot;question[question_text]&quot;:&quot;おいC++エヴァンゲリオン、C++ではなくSwiftを選ぶGoogleを許していいのか？&quot;,&quot;reask&quot;:true}" title="再度質問する" href="#"></a>
    <a class="rsp-eql-desktop streamItemOptions-reask icon-reask" data-gtm="{&quot;name&quot;:&quot;popup&quot;,&quot;meta&quot;:[&quot;question-popup&quot;,&quot;Questions&quot;,&quot;Reask&quot;]}" data-action="PopupOpen" data-url="/account/ask-friends" data-method="put" data-title="再度質問する" data-params="{&quot;question[question_text]&quot;:&quot;おいC++エヴァンゲリオン、C++ではなくSwiftを選ぶGoogleを許していいのか？&quot;,&quot;reask&quot;:true}" title="再度質問する" href="#"></a>
    <a title="今すぐ共有" class="streamItemOptions-share icon-share" data-action="PopupOpen" data-url="/EzoeRyou/answers/135859194711/share" data-gtm="{&quot;name&quot;:&quot;popup&quot;,&quot;meta&quot;:[&quot;share-topic&quot;,&quot;Share answer&quot;,&quot;New&quot;]}" href="#"></a>
  </div>
</div>
'''
        result = askfm.parser.parse(html)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 135859194711)
        self.assertEqual(result[0].question, u'おいC++エヴァンゲリオン、C++ではなくSwiftを選ぶGoogleを許していいのか？')
        self.assertEqual(result[0].answer, u'Swiftは\n罠がありそうで怖い。')

if __name__ == '__main__':
    unittest.main()

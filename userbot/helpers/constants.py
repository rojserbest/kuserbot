class First:
    ALIVE = "بەکە! ئەنەتە وە وەتەشی گە شینو تا ئاماتتە؟"
    REPO = "دەستبنێ <a href=\"https://github.com/rojserbest/kuserbot\">بە ئا ئێرە</a> بۆ کردنەوەی ڕیپۆی ئەم بۆتە."
    CREATOR = "لە ڕۆژێکی باراناویدا لە ژوورێکی زۆر گەرمدا بە دیار چا خواردنەوەوە لەلایەن <a href=\"https://github.com/rojserbest\">rojserbest</a>ـەوە دروستکرام."


class Weebify:
    NORMIE_FONT = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    WEEBY_FONT = ['卂', '乃', '匚', '刀', '乇', '下', '厶', '卄', '工', '丁', '长', '乚', '从', '𠘨', '口', '尸', '㔿', '尺', '丂', '丅',
                  '凵', 'リ', '山', '乂', '丫', '乙']


class Eval:
    RUNNING = "**پێدراو:**\n```{}```\n\n**شیکاردەکرێت...**"
    ERROR = "**پێدراو:**\n```{}```\n\n**هەڵە:**\n```{}```"
    SUCCESS = "**پێدراو:**\n```{}```\n\n**سەرکەوتن** | `None`"
    RESULT = "**پێدراو:**\n```{}```\n\n**ئەنجام:**\n```{}```"
    RESULT_FILE = "**پێدراو:**\n```{}```\n\n**ئەنجام:**\nفایلی `output.txt` ببینە ⤵"

    ERROR_LOG = (
        "**Evaluation Query**\n"
        "```{}```\n"
        "erred in chat \"[{}](t.me/c/{}/{})\" with error\n"
        "```{}```"
    )

    SUCCESS_LOG = (
        "Evaluation Query\n"
        "```{}```\n"
        "succeeded in \"[{}](t.me/c/{}/{})\""
    )

    RESULT_LOG = (
        "Evaluation Query\n"
        "```{}```\n"
        "executed in chat \"[{}](t.me/c/{}/{})\"."
    )


class WWW:
    SpeedTest = (
        "کاتی دەستپێکردنی تاقیکردنەوە:\n`{start}`\n\n"
        "پینگ:\n{ping} مچ\n\n"
        "داگرتن:\n{download}\n\n"
        "بەرزکردنەوە:\n{upload}\n\n"
        "دابینکەری خزمەتگوزاریی ئینتەرنێت:\n__{isp}__"
    )

    NearestDC = (
        "وڵات: `{}`\n"
        "نزیکترین داتاسەنتەر: `{}`\n"
        "ئەم داتاسەنتەرە: `{}`"
    )

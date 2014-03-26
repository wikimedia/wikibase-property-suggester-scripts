import requests

import xml.dom.minidom
from xml.dom.minidom import Node, parseString

edittokendata = {
	'action' : 'query',
	'prop' : 'info',
	'intoken' : 'edit',
	'generator' : 'allpages'
}

# result = requests.post("http://localhost/devrepo/core/api.php", data=edittokendata)

# tokendom = parseString(result.text)



propertyparams = {
    'action' : 'wbeditentity',
#    'data': '{"labels":{"en-gb":{"language":"en-gb","value":"Propertylabel4"}},"descriptions":{"en-gb":{"language":"en-gb","value":"Propertydescription"}},"datatype":"string"}',
    'data' : """
    "entities": {
        "P31": {
            "pageid": 3918489,
            "ns": 120,
            "title": "Property:P31",
            "lastrevid": 117307252,
            "modified": "2014-03-21T11:00:12Z",
            "id": "P31",
            "type": "property",
            "aliases": {
                "fr": [
                    {
                        "language": "fr",
                        "value": "est un"
                    },
                    {
                        "language": "fr",
                        "value": "est une"
                    },
                    {
                        "language": "fr",
                        "value": "nature"
                    },
                    {
                        "language": "fr",
                        "value": "instance de"
                    },
                    {
                        "language": "fr",
                        "value": "classe"
                    }
                ],
                "de": [
                    {
                        "language": "de",
                        "value": "ist Instanz von"
                    },
                    {
                        "language": "de",
                        "value": "Instanz von"
                    },
                    {
                        "language": "de",
                        "value": "ist eine Instanz von"
                    },
                    {
                        "language": "de",
                        "value": "war ein(e)"
                    }
                ],
                "he": [
                    {
                        "language": "he",
                        "value": "\u05d4\u05d9\u05d0"
                    },
                    {
                        "language": "he",
                        "value": "\u05d3\u05d5\u05d2\u05de\u05d4 \u05e9\u05dc"
                    },
                    {
                        "language": "he",
                        "value": "\u05de\u05e7\u05e8\u05d4 \u05e9\u05dc"
                    }
                ],
                "en": [
                    {
                        "language": "en",
                        "value": "is a"
                    },
                    {
                        "language": "en",
                        "value": "is an"
                    },
                    {
                        "language": "en",
                        "value": "rdf:type"
                    }
                ],
                "nb": [
                    {
                        "language": "nb",
                        "value": "element av"
                    },
                    {
                        "language": "nb",
                        "value": "eksempel p\u00e5"
                    },
                    {
                        "language": "nb",
                        "value": "utgave av"
                    },
                    {
                        "language": "nb",
                        "value": "er en/ei/et"
                    }
                ],
                "ru": [
                    {
                        "language": "ru",
                        "value": "\u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0441\u043e\u0431\u043e\u0439"
                    },
                    {
                        "language": "ru",
                        "value": "\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f"
                    },
                    {
                        "language": "ru",
                        "value": "\u0447\u0430\u0441\u0442\u043d\u044b\u0439 \u0441\u043b\u0443\u0447\u0430\u0439 \u0434\u043b\u044f"
                    },
                    {
                        "language": "ru",
                        "value": "\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043e\u0434\u043d\u0438\u043c \u0438\u0437 \u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u043e\u0432"
                    },
                    {
                        "language": "ru",
                        "value": "\u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u0438\u0442 \u043a\u043b\u0430\u0441\u0441\u0443"
                    },
                    {
                        "language": "ru",
                        "value": "\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043e\u0434\u043d\u0438\u043c \u0438\u0437"
                    },
                    {
                        "language": "ru",
                        "value": "\u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440 \u043e\u0442"
                    },
                    {
                        "language": "ru",
                        "value": "\u043a\u043b\u0430\u0441\u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430:"
                    },
                    {
                        "language": "ru",
                        "value": "\u0432\u0438\u0434 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438"
                    },
                    {
                        "language": "ru",
                        "value": "\u044d\u0442\u043e"
                    }
                ],
                "vi": [
                    {
                        "language": "vi",
                        "value": "l\u00e0"
                    },
                    {
                        "language": "vi",
                        "value": "l\u00e0 c\u00e1i"
                    }
                ],
                "ca": [
                    {
                        "language": "ca",
                        "value": "\u00e9s un"
                    },
                    {
                        "language": "ca",
                        "value": "\u00e9s una"
                    }
                ],
                "th": [
                    {
                        "language": "th",
                        "value": "\u0e04\u0e37\u0e2d"
                    }
                ],
                "uk": [
                    {
                        "language": "uk",
                        "value": "\u0454"
                    },
                    {
                        "language": "uk",
                        "value": "\u0446\u0435"
                    }
                ],
                "ilo": [
                    {
                        "language": "ilo",
                        "value": "ket maysa a"
                    },
                    {
                        "language": "ilo",
                        "value": "ket maysa nga"
                    }
                ],
                "fa": [
                    {
                        "language": "fa",
                        "value": "\u0647\u0633\u062a \u06cc\u06a9"
                    },
                    {
                        "language": "fa",
                        "value": "\u0627\u0633\u062a \u06cc\u06a9:"
                    },
                    {
                        "language": "fa",
                        "value": "\u06cc\u06a9 \u0645\u062b\u0627\u0644 \u0627\u0632"
                    },
                    {
                        "language": "fa",
                        "value": "\u0646\u0645\u0648\u0646\u0647 \u0627\u06cc \u0627\u0632"
                    },
                    {
                        "language": "fa",
                        "value": "\u0645\u062b\u0627\u0644\u06cc \u0627\u0632"
                    },
                    {
                        "language": "fa",
                        "value": "\u0627\u0633\u062a \u06cc\u06a9"
                    },
                    {
                        "language": "fa",
                        "value": "\u0632\u06cc\u0631\u0645\u062c\u0645\u0648\u0639\u0647\u0654"
                    }
                ],
                "ro": [
                    {
                        "language": "ro",
                        "value": "este o"
                    },
                    {
                        "language": "ro",
                        "value": "este un"
                    },
                    {
                        "language": "ro",
                        "value": "este o/un"
                    }
                ],
                "es": [
                    {
                        "language": "es",
                        "value": "es una"
                    },
                    {
                        "language": "es",
                        "value": "es un"
                    },
                    {
                        "language": "es",
                        "value": "es un/una"
                    }
                ],
                "it": [
                    {
                        "language": "it",
                        "value": "\u00e8 un"
                    },
                    {
                        "language": "it",
                        "value": "\u00e8 una"
                    }
                ],
                "en-ca": [
                    {
                        "language": "en-ca",
                        "value": "is a"
                    },
                    {
                        "language": "en-ca",
                        "value": "is an"
                    }
                ],
                "en-gb": [
                    {
                        "language": "en-gb",
                        "value": "is a"
                    },
                    {
                        "language": "en-gb",
                        "value": "is an"
                    }
                ],
                "ja": [
                    {
                        "language": "ja",
                        "value": "\u5206\u985e"
                    },
                    {
                        "language": "ja",
                        "value": "\u7a2e\u985e"
                    },
                    {
                        "language": "ja",
                        "value": "\u30a4\u30f3\u30b9\u30bf\u30f3\u30b9\u306e\u5143"
                    },
                    {
                        "language": "ja",
                        "value": "\u5b9f\u4f53\u306e\u5143"
                    },
                    {
                        "language": "ja",
                        "value": "is a"
                    },
                    {
                        "language": "ja",
                        "value": "is-a"
                    },
                    {
                        "language": "ja",
                        "value": "\u30af\u30e9\u30b9"
                    }
                ],
                "de-at": [
                    {
                        "language": "de-at",
                        "value": "ist ein"
                    },
                    {
                        "language": "de-at",
                        "value": "ist eine"
                    },
                    {
                        "language": "de-at",
                        "value": "ist Instanz von"
                    },
                    {
                        "language": "de-at",
                        "value": "Instanz von"
                    }
                ],
                "nl": [
                    {
                        "language": "nl",
                        "value": "instantie van"
                    },
                    {
                        "language": "nl",
                        "value": "exemplaar van"
                    }
                ],
                "de-ch": [
                    {
                        "language": "de-ch",
                        "value": "ist ein"
                    },
                    {
                        "language": "de-ch",
                        "value": "ist eine"
                    },
                    {
                        "language": "de-ch",
                        "value": "ist Instanz von"
                    },
                    {
                        "language": "de-ch",
                        "value": "Instanz von"
                    }
                ],
                "bar": [
                    {
                        "language": "bar",
                        "value": "is a"
                    },
                    {
                        "language": "bar",
                        "value": "is a Instanz vo"
                    },
                    {
                        "language": "bar",
                        "value": "Instanz vo"
                    }
                ],
                "sh": [
                    {
                        "language": "sh",
                        "value": "je"
                    },
                    {
                        "language": "sh",
                        "value": "su"
                    },
                    {
                        "language": "sh",
                        "value": "jest"
                    }
                ],
                "bg": [
                    {
                        "language": "bg",
                        "value": "e"
                    }
                ],
                "zh": [
                    {
                        "language": "zh",
                        "value": "\u662f\u4e00\u4e2a"
                    },
                    {
                        "language": "zh",
                        "value": "\u6027\u8d28"
                    },
                    {
                        "language": "zh",
                        "value": "\u662f\u4e00\u500b"
                    },
                    {
                        "language": "zh",
                        "value": "\u6027\u8cea"
                    }
                ],
                "zh-hant": [
                    {
                        "language": "zh-hant",
                        "value": "\u662f\u4e00\u500b"
                    }
                ],
                "yi": [
                    {
                        "language": "yi",
                        "value": "\u05d0\u05d9\u05d6 \u05d0"
                    },
                    {
                        "language": "yi",
                        "value": "\u05d0\u05d9\u05d6 \u05d0\u05df"
                    }
                ],
                "cs": [
                    {
                        "language": "cs",
                        "value": "je"
                    }
                ],
                "fi": [
                    {
                        "language": "fi",
                        "value": "on"
                    },
                    {
                        "language": "fi",
                        "value": "kuuluu ryhm\u00e4\u00e4n"
                    }
                ],
                "be-tarask": [
                    {
                        "language": "be-tarask",
                        "value": "\u0432\u044b\u043a\u043b\u044e\u0447\u043d\u044b \u0432\u044b\u043f\u0430\u0434\u0430\u043a \u043f\u0430\u043d\u044f\u0442\u043a\u0443"
                    }
                ],
                "pt": [
                    {
                        "language": "pt",
                        "value": "\u00e9 um"
                    },
                    {
                        "language": "pt",
                        "value": "\u00e9 uma"
                    },
                    {
                        "language": "pt",
                        "value": "natureza do elemento"
                    }
                ],
                "zh-hk": [
                    {
                        "language": "zh-hk",
                        "value": "\u6027\u8cea"
                    }
                ],
                "te": [
                    {
                        "language": "te",
                        "value": "\u0c30\u0c15\u0c02"
                    },
                    {
                        "language": "te",
                        "value": "\u0c07\u0c26\u0c3f \u0c12\u0c15"
                    }
                ],
                "or": [
                    {
                        "language": "or",
                        "value": "\u0b09\u0b26\u0b3e\u0b39\u0b30\u0b23"
                    }
                ],
                "hu": [
                    {
                        "language": "hu",
                        "value": "kateg\u00f3ria"
                    },
                    {
                        "language": "hu",
                        "value": "p\u00e9ld\u00e1nya ennek"
                    },
                    {
                        "language": "hu",
                        "value": "ez egy"
                    }
                ]
            },
            "labels": {
                "en": {
                    "language": "en",
                    "value": "instance of"
                },
                "fr": {
                    "language": "fr",
                    "value": "nature de l'\u00e9l\u00e9ment"
                },
                "de": {
                    "language": "de",
                    "value": "ist ein(e)"
                },
                "it": {
                    "language": "it",
                    "value": "istanza di"
                },
                "pt-br": {
                    "language": "pt-br",
                    "value": "inst\u00e2ncia de"
                },
                "eo": {
                    "language": "eo",
                    "value": "estas"
                },
                "he": {
                    "language": "he",
                    "value": "\u05d4\u05d5\u05d0"
                },
                "es": {
                    "language": "es",
                    "value": "instancia de"
                },
                "zh-hans": {
                    "language": "zh-hans",
                    "value": "\u6027\u8d28"
                },
                "fi": {
                    "language": "fi",
                    "value": "esiintym\u00e4 kohteesta"
                },
                "hu": {
                    "language": "hu",
                    "value": "p\u00e9lda erre"
                },
                "ru": {
                    "language": "ru",
                    "value": "\u044d\u0442\u043e \u0447\u0430\u0441\u0442\u043d\u044b\u0439 \u0441\u043b\u0443\u0447\u0430\u0439 \u043f\u043e\u043d\u044f\u0442\u0438\u044f"
                },
                "hr": {
                    "language": "hr",
                    "value": "je"
                },
                "zh-hant": {
                    "language": "zh-hant",
                    "value": "\u6027\u8cea"
                },
                "nl": {
                    "language": "nl",
                    "value": "is een"
                },
                "el": {
                    "language": "el",
                    "value": "\u03b5\u03af\u03bd\u03b1\u03b9"
                },
                "pl": {
                    "language": "pl",
                    "value": "jest to"
                },
                "sr": {
                    "language": "sr",
                    "value": "\u0458\u0435"
                },
                "ca": {
                    "language": "ca",
                    "value": "\u00e9s inst\u00e0ncia de"
                },
                "cs": {
                    "language": "cs",
                    "value": "instance (\u010deho)"
                },
                "nb": {
                    "language": "nb",
                    "value": "instans av"
                },
                "pt": {
                    "language": "pt",
                    "value": "inst\u00e2ncia de"
                },
                "ilo": {
                    "language": "ilo",
                    "value": "pagarigan iti"
                },
                "sl": {
                    "language": "sl",
                    "value": "je"
                },
                "be": {
                    "language": "be",
                    "value": "\u0433\u044d\u0442\u0430"
                },
                "ko": {
                    "language": "ko",
                    "value": "\uc885\ub958"
                },
                "nn": {
                    "language": "nn",
                    "value": "er ein/ei/eit"
                },
                "vi": {
                    "language": "vi",
                    "value": "l\u00e0 m\u1ed9t"
                },
                "be-tarask": {
                    "language": "be-tarask",
                    "value": "\u0430\u0441\u043e\u0431\u043d\u044b \u0432\u044b\u043f\u0430\u0434\u0430\u043a \u043f\u0430\u043d\u044f\u0442\u043a\u0443"
                },
                "bs": {
                    "language": "bs",
                    "value": "je"
                },
                "th": {
                    "language": "th",
                    "value": "\u0e40\u0e1b\u0e47\u0e19"
                },
                "uk": {
                    "language": "uk",
                    "value": "\u0454 \u043e\u0434\u043d\u0438\u043c \u0456\u0437"
                },
                "en-gb": {
                    "language": "en-gb",
                    "value": "instance of"
                },
                "en-ca": {
                    "language": "en-ca",
                    "value": "instance of"
                },
                "ja": {
                    "language": "ja",
                    "value": "\u4ee5\u4e0b\u306e\u5b9f\u4f53"
                },
                "uz": {
                    "language": "uz",
                    "value": "bu"
                },
                "lv": {
                    "language": "lv",
                    "value": "ir"
                },
                "la": {
                    "language": "la",
                    "value": "est"
                },
                "fa": {
                    "language": "fa",
                    "value": "\u06cc\u06a9 \u0646\u0645\u0648\u0646\u0647 \u0627\u0632"
                },
                "sv": {
                    "language": "sv",
                    "value": "\u00e4r en/ett"
                },
                "nds": {
                    "language": "nds",
                    "value": "is en"
                },
                "ro": {
                    "language": "ro",
                    "value": "este un/o"
                },
                "ta": {
                    "language": "ta",
                    "value": "\u0b86\u0ba9\u0ba4\u0bc1"
                },
                "min": {
                    "language": "min",
                    "value": "adolah"
                },
                "id": {
                    "language": "id",
                    "value": "adalah"
                },
                "gl": {
                    "language": "gl",
                    "value": "\u00e9 un/unha"
                },
                "is": {
                    "language": "is",
                    "value": "er"
                },
                "af": {
                    "language": "af",
                    "value": "is 'n"
                },
                "ka": {
                    "language": "ka",
                    "value": "\u10d0\u10e0\u10d8\u10e1"
                },
                "de-at": {
                    "language": "de-at",
                    "value": "ist eine Instanz von"
                },
                "da": {
                    "language": "da",
                    "value": "er en/et"
                },
                "sco": {
                    "language": "sco",
                    "value": "instance o"
                },
                "sk": {
                    "language": "sk",
                    "value": "je"
                },
                "de-ch": {
                    "language": "de-ch",
                    "value": "ist eine Instanz von"
                },
                "bar": {
                    "language": "bar",
                    "value": "is a Instanz vo"
                },
                "simple": {
                    "language": "simple",
                    "value": "instance of"
                },
                "bn": {
                    "language": "bn",
                    "value": "\u09a8\u09bf\u09a6\u09b0\u09cd\u09b6\u09a8"
                },
                "lmo": {
                    "language": "lmo",
                    "value": "l'\u00e8 un(a)"
                },
                "nds-nl": {
                    "language": "nds-nl",
                    "value": "is n"
                },
                "sh": {
                    "language": "sh",
                    "value": "je(su)"
                },
                "br": {
                    "language": "br",
                    "value": "elfenn eus"
                },
                "bg": {
                    "language": "bg",
                    "value": "\u0435\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440 \u043d\u0430"
                },
                "mr": {
                    "language": "mr",
                    "value": "\u092a\u094d\u0930\u0915\u093e\u0930"
                },
                "ckb": {
                    "language": "ckb",
                    "value": "\u0646\u0645\u0648\u0648\u0646\u06d5\u06cc\u06d5\u06a9 \u0644\u06d5"
                },
                "ar": {
                    "language": "ar",
                    "value": "\u0647\u0648"
                },
                "et": {
                    "language": "et",
                    "value": "on"
                },
                "no": {
                    "language": "no",
                    "value": "er en"
                },
                "pcd": {
                    "language": "pcd",
                    "value": "est un"
                },
                "tr": {
                    "language": "tr",
                    "value": "bir"
                },
                "hi": {
                    "language": "hi",
                    "value": "\u0909\u0926\u0939\u093e\u0930\u0923 \u0939\u0948"
                },
                "sr-ec": {
                    "language": "sr-ec",
                    "value": "\u0458\u0435"
                },
                "co": {
                    "language": "co",
                    "value": "istanza di"
                },
                "oc": {
                    "language": "oc",
                    "value": "natura de l'element"
                },
                "mk": {
                    "language": "mk",
                    "value": "\u0435"
                },
                "yi": {
                    "language": "yi",
                    "value": "\u05e4\u05bf\u05d0\u05b7\u05dc"
                },
                "zh": {
                    "language": "zh",
                    "value": "\u6027\u8d28"
                },
                "jbo": {
                    "language": "jbo",
                    "value": "serese mupli"
                },
                "gu": {
                    "language": "gu",
                    "value": "\u0a89\u0aa6\u0abe\u0ab9\u0ab0\u0aa3"
                },
                "zh-cn": {
                    "language": "zh-cn",
                    "value": "\u6027\u8d28"
                },
                "ms": {
                    "language": "ms",
                    "value": "contoh"
                },
                "tl": {
                    "language": "tl",
                    "value": "ay halimbawa ng"
                },
                "zh-tw": {
                    "language": "zh-tw",
                    "value": "\u6027\u8cea"
                },
                "rm": {
                    "language": "rm",
                    "value": "\u00e8 in(a)"
                },
                "ksh": {
                    "language": "ksh",
                    "value": "es e Beischpell f\u00f6r e(n(e))"
                },
                "lb": {
                    "language": "lb",
                    "value": "geh\u00e9iert zu"
                },
                "csb": {
                    "language": "csb",
                    "value": "to je"
                },
                "ts": {
                    "language": "ts",
                    "value": "Nchumu"
                },
                "gsw": {
                    "language": "gsw",
                    "value": "isch e"
                },
                "mzn": {
                    "language": "mzn",
                    "value": "\u062f\u0650\u0644\u0650\u0648\u0633"
                },
                "zh-hk": {
                    "language": "zh-hk",
                    "value": "\u5c6c\u6027"
                },
                "te": {
                    "language": "te",
                    "value": "\u0c05\u0c02\u0c36"
                },
                "de-formal": {
                    "language": "de-formal",
                    "value": "ist ein/eine"
                },
                "or": {
                    "language": "or",
                    "value": "\u0b26\u0b43\u0b37\u0b4d\u0b1f\u0b3e\u0b28\u0b4d\u0b24"
                },
                "sr-el": {
                    "language": "sr-el",
                    "value": "je"
                },
                "stq": {
                    "language": "stq",
                    "value": "is n(e)"
                }
            },
            "descriptions": {
                "en": {
                    "language": "en",
                    "value": "this item is a concrete object (instance) of this class, category or object group"
                },
                "it": {
                    "language": "it",
                    "value": "questo elemento \u00e8 un'istanza di questa classe, categoria o gruppo di oggetti"
                },
                "fr": {
                    "language": "fr",
                    "value": "nature de, expression de ou exemplaire de"
                },
                "pt-br": {
                    "language": "pt-br",
                    "value": "este item \u00e9 uma inst\u00e2ncia deste outro item"
                },
                "hu": {
                    "language": "hu",
                    "value": "az elem a m\u00e1sik elem p\u00e9ld\u00e1nya"
                },
                "hr": {
                    "language": "hr",
                    "value": "ova stavka je primjer ove druge stavke"
                },
                "de": {
                    "language": "de",
                    "value": "Auspr\u00e4gung oder Exemplar einer Sache"
                },
                "el": {
                    "language": "el",
                    "value": "\u03b1\u03c5\u03c4\u03cc \u03c4\u03bf \u03b1\u03bd\u03c4\u03b9\u03ba\u03b5\u03af\u03bc\u03b5\u03bd\u03bf \u03b5\u03af\u03bd\u03b1\u03b9 \u03bc\u03b9\u03b1 \u03ad\u03ba\u03c6\u03c1\u03b1\u03c3\u03b7 \u03b1\u03c5\u03c4\u03bf\u03cd \u03c4\u03bf\u03c5 \u03ac\u03bb\u03bb\u03bf\u03c5 \u03b1\u03bd\u03c4\u03b9\u03ba\u03b5\u03af\u03bc\u03b5\u03bd\u03bf\u03c5"
                },
                "fi": {
                    "language": "fi",
                    "value": "kohde, johon ominaisuus liitet\u00e4\u00e4n, on esiintym\u00e4 ominaisuuden arvoksi asetettavasta kohteesta"
                },
                "ilo": {
                    "language": "ilo",
                    "value": "daytoy a banag ket maysa a pagarigan iti daytoy a sabali a banag"
                },
                "nb": {
                    "language": "nb",
                    "value": "dette elementet er et konkret objekt/eksemplar (instans) av denne klassen, kategorien eller objektgruppen"
                },
                "es": {
                    "language": "es",
                    "value": "este elemento es un ejemplar de otro elemento"
                },
                "vi": {
                    "language": "vi",
                    "value": "kho\u1ea3n m\u1ee5c n\u00e0y l\u00e0 m\u1ed9t th\u1ef1c th\u1ec3 c\u1ee7a kho\u1ea3n m\u1ee5c kia"
                },
                "be-tarask": {
                    "language": "be-tarask",
                    "value": "\u0430\u0433\u0443\u043b\u044c\u043d\u0430\u0435 \u0430\u0437\u043d\u0430\u0447\u044d\u043d\u044c\u043d\u0435, \u0447\u044b\u043c \u0437\u044c\u044f\u045e\u043b\u044f\u0435\u0446\u0446\u0430 \u0430\u0431\u2019\u0435\u043a\u0442"
                },
                "ja": {
                    "language": "ja",
                    "value": "\u3053\u306e\u9805\u76ee\u3092\u30a4\u30f3\u30b9\u30bf\u30f3\u30b9\uff08\u5b9f\u4f53\uff09\u3068\u3059\u308b\u7a2e\u985e\u30fb\u6982\u5ff5"
                },
                "en-gb": {
                    "language": "en-gb",
                    "value": "this item is an instance of this other item"
                },
                "en-ca": {
                    "language": "en-ca",
                    "value": "the subject is an instance of the object"
                },
                "pl": {
                    "language": "pl",
                    "value": "stanowi przyk\u0142ad innego obiektu"
                },
                "lv": {
                    "language": "lv",
                    "value": "\u0161\u012b vien\u012bba ir \u0161\u012bs citas vien\u012bbas instance"
                },
                "ca": {
                    "language": "ca",
                    "value": "aquest element \u00e9s un objecte concret (inst\u00e0ncia) d'aquesta classe, categoria o grup d'objectes"
                },
                "sv": {
                    "language": "sv",
                    "value": "\u00e4r en instans av eller underkategori till"
                },
                "fa": {
                    "language": "fa",
                    "value": "\u0622\u06cc\u062a\u0645 \u06cc\u06a9 \u0646\u0648\u0639 ... \u0627\u0633\u062a"
                },
                "gl": {
                    "language": "gl",
                    "value": "o elemento \u00e9 unha instancia doutro elemento"
                },
                "is": {
                    "language": "is",
                    "value": "\u00deessi hlutur er d\u00e6mi um annan hlut"
                },
                "nl": {
                    "language": "nl",
                    "value": "dit item is een exemplaar (instantie) van deze groep elementen"
                },
                "ru": {
                    "language": "ru",
                    "value": "\u0434\u0430\u043d\u043d\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0441\u043e\u0431\u043e\u0439 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043e\u0431\u044a\u0435\u043a\u0442 (\u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440 / \u0447\u0430\u0441\u0442\u043d\u044b\u0439 \u0441\u043b\u0443\u0447\u0430\u0439) \u043a\u043b\u0430\u0441\u0441\u0430, \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0438\u043b\u0438 \u0433\u0440\u0443\u043f\u043f\u044b \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432"
                },
                "uk": {
                    "language": "uk",
                    "value": "\u0446\u0435\u0439 \u0435\u043b\u0435\u043c\u0435\u043d\u0442 \u0454 \u0447\u0430\u0441\u0442\u0438\u043d\u043e\u044e \u043c\u043d\u043e\u0436\u0438\u043d\u0438 \u0456\u043d\u0448\u0438\u0445 \u0435\u043b\u0435\u043c\u0435\u043d\u0442\u0456\u0432"
                },
                "de-at": {
                    "language": "de-at",
                    "value": "Auspr\u00e4gung oder Exemplar einer Sache"
                },
                "da": {
                    "language": "da",
                    "value": "dette emne er et konkret objekt af denne kategori, klasse eller objektgruppe."
                },
                "ro": {
                    "language": "ro",
                    "value": "acest element este un exemplar din clasa definit\u0103 de acel element"
                },
                "de-ch": {
                    "language": "de-ch",
                    "value": "Auspr\u00e4gung oder Exemplar einer Sache"
                },
                "nds-nl": {
                    "language": "nds-nl",
                    "value": "dit item is n eksemplaor/instansie van t tweede item (Veurbeeld: \"Mark Rutte\" is nen \"politieker\")"
                },
                "he": {
                    "language": "he",
                    "value": "\u05d4\u05e0\u05d3\u05d5\u05df \u05d4\u05d5\u05d0 \u05de\u05e7\u05e8\u05d4 \u05e9\u05dc"
                },
                "bg": {
                    "language": "bg",
                    "value": "\u043e\u0431\u0435\u043a\u0442\u044a\u0442 \u0435 \u0435\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440 \u043e\u0442 \u0434\u0430\u0434\u0435\u043d \u043a\u043b\u0430\u0441"
                },
                "hi": {
                    "language": "hi",
                    "value": "\u092f\u0939 \u0906\u0907\u091f\u092e \u0907\u0938 \u0905\u0928\u094d\u092f \u0906\u0907\u091f\u092e \u0915\u093e \u0909\u0926\u0939\u093e\u0930\u0923 \u0939\u0948"
                },
                "sr": {
                    "language": "sr",
                    "value": "\u043e\u0432\u0430 \u0441\u0442\u0430\u0432\u043a\u0430 \u0458\u0435 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u0430\u043d \u043e\u0431\u0458\u0435\u043a\u0430\u0442 (\u0438\u043d\u0441\u0442\u0430\u043d\u0446\u0430) \u043a\u043b\u0430\u0441\u0435, \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0435 \u0438\u043b\u0438 \u0433\u0440\u0443\u043f\u0435 \u043e\u0431\u0458\u0435\u043a\u0430\u0442\u0430"
                },
                "sr-ec": {
                    "language": "sr-ec",
                    "value": "\u043e\u0432\u0430 \u0441\u0442\u0430\u0432\u043a\u0430 \u0458\u0435 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u0430\u043d \u043e\u0431\u0458\u0435\u043a\u0430\u0442 (\u0438\u043d\u0441\u0442\u0430\u043d\u0446\u0430) \u043a\u043b\u0430\u0441\u0435, \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0435 \u0438\u043b\u0438 \u0433\u0440\u0443\u043f\u0435 \u043e\u0431\u0458\u0435\u043a\u0430\u0442\u0430"
                },
                "mk": {
                    "language": "mk",
                    "value": "\u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043e\u0442 \u0435 \u043f\u0440\u0438\u043c\u0435\u0440\u043e\u043a/\u0441\u043b\u0443\u0447\u0430\u0458 \u043d\u0430 \u0434\u0440\u0443\u0433 \u043f\u0440\u0435\u0434\u043c\u0435\u0442"
                },
                "cs": {
                    "language": "cs",
                    "value": "tato polo\u017eka je jedna konkr\u00e9tn\u00ed v\u011bc (exempl\u00e1\u0159, p\u0159\u00edklad) pat\u0159\u00edc\u00ed do t\u00e9to t\u0159\u00eddy, kategorie nebo skupiny p\u0159edm\u011bt\u016f"
                },
                "gu": {
                    "language": "gu",
                    "value": "\u0a86 \u0ab2\u0ac7\u0a96 \u0a86 \u0aaa\u0acd\u0ab0\u0a95\u0abe\u0ab0 \u0a85\u0aa5\u0ab5\u0abe \u0ab6\u0acd\u0ab0\u0ac7\u0aa3\u0ac0\u0aa8\u0abe \u0a85\u0aa8\u0acd\u0aaf \u0ab2\u0ac7\u0a96\u0acb\u0aa8\u0ac1\u0a82 \u0ab8\u0a9a\u0acb\u0a9f \u0a89\u0aa6\u0abe\u0ab9\u0ab0\u0aa3 \u0a9b\u0ac7."
                },
                "ksh": {
                    "language": "ksh",
                    "value": "di Saach es ene beschtemmpte, konkrete J\u00e4\u00e4jeschtand vun d\u00e4 Zoot, udder Jropp, udder d\u00e4 Aat"
                },
                "eo": {
                    "language": "eo",
                    "value": "tiu \u0109i ero estas konkreta a\u0135o (instanco) de tiu \u0109i klaso, kategorio a\u016d objektogrupo"
                },
                "ko": {
                    "language": "ko",
                    "value": "\ud56d\ubaa9\uc774 \uc18d\ud558\ub294 \uacf3"
                },
                "oc": {
                    "language": "oc",
                    "value": "natura de, expression de o exemplar de"
                },
                "mzn": {
                    "language": "mzn",
                    "value": "\u0622\u06cc\u062a\u0645 \u062c\u0648\u0631"
                },
                "zh": {
                    "language": "zh",
                    "value": "\u9805\u6240\u5c6c\u7684\uff0c\u4ee5\u9805\u70ba\u5be6\u4f8b\u7684\u985e\u5225"
                },
                "zh-hk": {
                    "language": "zh-hk",
                    "value": "\u9805\u6240\u5c6c\u7684\uff0c\u4ee5\u9805\u70ba\u5be6\u4f8b\u7684\u985e\u5225"
                },
                "pt": {
                    "language": "pt",
                    "value": "este item \u00e9 uma inst\u00e2ncia deste outro item"
                },
                "zh-hans": {
                    "language": "zh-hans",
                    "value": "\u9879\u6240\u5c5e\u7684\uff0c\u4ee5\u9879\u4e3a\u5b9e\u4f8b\u7684\u7c7b\u522b"
                },
                "zh-cn": {
                    "language": "zh-cn",
                    "value": "\u9879\u6240\u5c5e\u7684\uff0c\u4ee5\u9879\u4e3a\u5b9e\u4f8b\u7684\u7c7b\u522b"
                },
                "id": {
                    "language": "id",
                    "value": "item ini adalah obyek konkret (instans) dari kelas, kategori, atau kelompok obyek ini"
                },
                "sr-el": {
                    "language": "sr-el",
                    "value": "ova stavka je konkretan objekat (instanca) klase, kategorije ili grupe objekata"
                }
            },
            "datatype": "wikibase-item"
        }
    }""",
    'new' : 'property',
    'token' : "+\\"}
   	# token is here http://localhost/devrepo/core/api.php?action=query&prop=info&intoken=edit&generator=allpages&format=json
   	



#edittoken = returnData['query']['pages']['1']['edittoken'] 


# login = {
# 	'action' : 'login',
# 	'lgname' : 'root2',
# 	'lgpassword' : 'root'
# }

#resultLogin = requests.post("http://localhost/devrepo/core/api.php", data=login)

#print resultLogin.text.encode("utf-8");

#then you must use the following to get the edittoken: 



result = requests.post("http://localhost/devrepo/core/api.php", data=propertyparams)

print result.text.encode("utf-8")

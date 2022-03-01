def tf_idf(data=[], seed_data=[]):
    # print("===========TF-IDF==========")
    # print(seed_data)
    # print(data)
    for i in range(len(data)):
        data[i]['tf_idf'] = '0.432431'
    return data


test_data = [
    {
        "created_at": "Thu Feb 10 22:17:29 +0000 2022",
        "id": 1491899146177028000,
        "id_str": "1491899146177028098",
        "text": "The Nets are waiving DeAndre Bembry to create roster room for the trade today, sources tell ESPN.",
        "truncated": False,
        "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [],
            "urls": []
        },
        "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user": {
            "id": 50323173,
            "id_str": "50323173",
            "name": "Adrian Wojnaroawski",
            "screen_name": "wojespn",
            "location": "St. Bonaventure, NY",
            "description": "ESPN Senior NBA Insider",
            "url": "https://t.co/BSi8UGrj5q",
            "entities": {
                "url": {
                    "urls": [
                        {
                            "url": "https://t.co/BSi8UGrj5q",
                            "expanded_url": "http://www.espn.com",
                            "display_url": "espn.com",
                            "indices": [
                                0,
                                23
                            ]
                        }
                    ]
                },
                "description": {
                    "urls": []
                }
            },
            "protected": False,
            "followers_count": 5207870,
            "friends_count": 1855,
            "listed_count": 34021,
            "created_at": "Wed Jun 24 14:43:40 +0000 2009",
            "favourites_count": 10108,
            "utc_offset": None,
            "time_zone": None,
            "geo_enabled": True,
            "verified": True,
            "statuses_count": 21758,
            "lang": None,
            "contributors_enabled": False,
            "is_translator": False,
            "is_translation_enabled": False,
            "profile_background_color": "642D8B",
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_tile": True,
            "profile_image_url": "http://pbs.twimg.com/profile_images/1264902234703265794/lC3YnIYF_normal.jpg",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/1264902234703265794/lC3YnIYF_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/50323173/1501272451",
            "profile_link_color": "FF0000",
            "profile_sidebar_border_color": "FFFFFF",
            "profile_sidebar_fill_color": "DDFFCC",
            "profile_text_color": "333333",
            "profile_use_background_image": True,
            "has_extended_profile": False,
            "default_profile": False,
            "default_profile_image": False,
            "following": None,
            "follow_request_sent": None,
            "notifications": None,
            "translator_type": "none",
            "withheld_in_countries": []
        },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "is_quote_status": False,
        "retweet_count": 982,
        "favorite_count": 15092,
        "favorited": False,
        "retweeted": False,
        "lang": "en"
    },
    {
        "created_at": "Thu Feb 10 21:11:41 +0000 2022",
        "id": 1491882588193136600,
        "id_str": "1491882588193136644",
        "text": "RT @SportsCenter: The new-look 76ers 👀\n\n(via @wojespn) https://t.co/oXhZusHLpB",
        "truncated": False,
        "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [
                {
                    "screen_name": "SportsCenter",
                    "name": "SportsCenter",
                    "id": 26257166,
                    "id_str": "26257166",
                    "indices": [
                        3,
                        16
                    ]
                },
                {
                    "screen_name": "wojespn",
                    "name": "Adrian Wojnarowski",
                    "id": 50323173,
                    "id_str": "50323173",
                    "indices": [
                        45,
                        53
                    ]
                }
            ],
            "urls": [],
            "media": [
                {
                    "id": 1491840563368415200,
                    "id_str": "1491840563368415240",
                    "indices": [
                        55,
                        78
                    ],
                    "media_url": "http://pbs.twimg.com/media/FLQVFpkX0Ag0Qxs.jpg",
                    "media_url_https": "https://pbs.twimg.com/media/FLQVFpkX0Ag0Qxs.jpg",
                    "url": "https://t.co/oXhZusHLpB",
                    "display_url": "pic.twitter.com/oXhZusHLpB",
                    "expanded_url": "https://twitter.com/SportsCenter/status/1491840569102020609/photo/1",
                    "type": "photo",
                    "sizes": {
                        "large": {
                            "w": 1080,
                            "h": 1080,
                            "resize": "fit"
                        },
                        "thumb": {
                            "w": 150,
                            "h": 150,
                            "resize": "crop"
                        },
                        "small": {
                            "w": 680,
                            "h": 680,
                            "resize": "fit"
                        },
                        "medium": {
                            "w": 1080,
                            "h": 1080,
                            "resize": "fit"
                        }
                    },
                    "source_status_id": 1491840569102020600,
                    "source_status_id_str": "1491840569102020609",
                    "source_user_id": 26257166,
                    "source_user_id_str": "26257166"
                }
            ]
        },
        "extended_entities": {
            "media": [
                {
                    "id": 1491840563368415200,
                    "id_str": "1491840563368415240",
                    "indices": [
                        55,
                        78
                    ],
                    "media_url": "http://pbs.twimg.com/media/FLQVFpkX0Ag0Qxs.jpg",
                    "media_url_https": "https://pbs.twimg.com/media/FLQVFpkX0Ag0Qxs.jpg",
                    "url": "https://t.co/oXhZusHLpB",
                    "display_url": "pic.twitter.com/oXhZusHLpB",
                    "expanded_url": "https://twitter.com/SportsCenter/status/1491840569102020609/photo/1",
                    "type": "photo",
                    "sizes": {
                        "large": {
                            "w": 1080,
                            "h": 1080,
                            "resize": "fit"
                        },
                        "thumb": {
                            "w": 150,
                            "h": 150,
                            "resize": "crop"
                        },
                        "small": {
                            "w": 680,
                            "h": 680,
                            "resize": "fit"
                        },
                        "medium": {
                            "w": 1080,
                            "h": 1080,
                            "resize": "fit"
                        }
                    },
                    "source_status_id": 1491840569102020600,
                    "source_status_id_str": "1491840569102020609",
                    "source_user_id": 26257166,
                    "source_user_id_str": "26257166"
                }
            ]
        },
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user": {
            "id": 50323173,
            "id_str": "50323173",
            "name": "Adrian Wojnarowski",
            "screen_name": "wojespn",
            "location": "St. Bonaventure, NY",
            "description": "ESPN Senior NBA Insider",
            "url": "https://t.co/BSi8UGrj5q",
            "entities": {
                "url": {
                    "urls": [
                        {
                            "url": "https://t.co/BSi8UGrj5q",
                            "expanded_url": "http://www.espn.com",
                            "display_url": "espn.com",
                            "indices": [
                                0,
                                23
                            ]
                        }
                    ]
                },
                "description": {
                    "urls": []
                }
            },
            "protected": False,
            "followers_count": 5207870,
            "friends_count": 1855,
            "listed_count": 34021,
            "created_at": "Wed Jun 24 14:43:40 +0000 2009",
            "favourites_count": 10108,
            "utc_offset": None,
            "time_zone": None,
            "geo_enabled": True,
            "verified": True,
            "statuses_count": 21758,
            "lang": None,
            "contributors_enabled": False,
            "is_translator": False,
            "is_translation_enabled": False,
            "profile_background_color": "642D8B",
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_tile": True,
            "profile_image_url": "http://pbs.twimg.com/profile_images/1264902234703265794/lC3YnIYF_normal.jpg",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/1264902234703265794/lC3YnIYF_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/50323173/1501272451",
            "profile_link_color": "FF0000",
            "profile_sidebar_border_color": "FFFFFF",
            "profile_sidebar_fill_color": "DDFFCC",
            "profile_text_color": "333333",
            "profile_use_background_image": True,
            "has_extended_profile": False,
            "default_profile": False,
            "default_profile_image": False,
            "following": None,
            "follow_request_sent": None,
            "notifications": None,
            "translator_type": "none",
            "withheld_in_countries": []
        },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "retweeted_status": {
            "created_at": "Thu Feb 10 18:24:43 +0000 2022",
            "id": 1491840569102020600,
            "id_str": "1491840569102020609",
            "text": "The new-look 76ers 👀\n\n(via @wojespn) https://t.co/oXhZusHLpB",
            "truncated": False,
            "entities": {
                "hashtags": [],
                "symbols": [],
                "user_mentions": [
                    {
                        "screen_name": "wojespn",
                        "name": "Adrian Wojnarowski",
                        "id": 50323173,
                        "id_str": "50323173",
                        "indices": [
                            27,
                            35
                        ]
                    }
                ],
                "urls": [],
                "media": [
                    {
                        "id": 1491840563368415200,
                        "id_str": "1491840563368415240",
                        "indices": [
                            37,
                            60
                        ],
                        "media_url": "http://pbs.twimg.com/media/FLQVFpkX0Ag0Qxs.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/FLQVFpkX0Ag0Qxs.jpg",
                        "url": "https://t.co/oXhZusHLpB",
                        "display_url": "pic.twitter.com/oXhZusHLpB",
                        "expanded_url": "https://twitter.com/SportsCenter/status/1491840569102020609/photo/1",
                        "type": "photo",
                        "sizes": {
                            "large": {
                                "w": 1080,
                                "h": 1080,
                                "resize": "fit"
                            },
                            "thumb": {
                                "w": 150,
                                "h": 150,
                                "resize": "crop"
                            },
                            "small": {
                                "w": 680,
                                "h": 680,
                                "resize": "fit"
                            },
                            "medium": {
                                "w": 1080,
                                "h": 1080,
                                "resize": "fit"
                            }
                        }
                    }
                ]
            },
            "extended_entities": {
                "media": [
                    {
                        "id": 1491840563368415200,
                        "id_str": "1491840563368415240",
                        "indices": [
                            37,
                            60
                        ],
                        "media_url": "http://pbs.twimg.com/media/FLQVFpkX0Ag0Qxs.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/FLQVFpkX0Ag0Qxs.jpg",
                        "url": "https://t.co/oXhZusHLpB",
                        "display_url": "pic.twitter.com/oXhZusHLpB",
                        "expanded_url": "https://twitter.com/SportsCenter/status/1491840569102020609/photo/1",
                        "type": "photo",
                        "sizes": {
                            "large": {
                                "w": 1080,
                                "h": 1080,
                                "resize": "fit"
                            },
                            "thumb": {
                                "w": 150,
                                "h": 150,
                                "resize": "crop"
                            },
                            "small": {
                                "w": 680,
                                "h": 680,
                                "resize": "fit"
                            },
                            "medium": {
                                "w": 1080,
                                "h": 1080,
                                "resize": "fit"
                            }
                        }
                    }
                ]
            },
            "source": "<a href=\"https://www.sprinklr.com\" rel=\"nofollow\">Sprinklr</a>",
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user": {
                "id": 26257166,
                "id_str": "26257166",
                "name": "SportsCenter",
                "screen_name": "SportsCenter",
                "location": "",
                "description": "Download the ESPN App ⬇️",
                "url": "https://t.co/RqqkIx8GI7",
                "entities": {
                    "url": {
                        "urls": [
                            {
                                "url": "https://t.co/RqqkIx8GI7",
                                "expanded_url": "http://es.pn/app",
                                "display_url": "es.pn/app",
                                "indices": [
                                    0,
                                    23
                                ]
                            }
                        ]
                    },
                    "description": {
                        "urls": []
                    }
                },
                "protected": False,
                "followers_count": 39472884,
                "friends_count": 731,
                "listed_count": 44197,
                "created_at": "Tue Mar 24 15:28:02 +0000 2009",
                "favourites_count": 1982,
                "utc_offset": None,
                "time_zone": None,
                "geo_enabled": True,
                "verified": True,
                "statuses_count": 132431,
                "lang": None,
                "contributors_enabled": False,
                "is_translator": False,
                "is_translation_enabled": True,
                "profile_background_color": "131516",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
                "profile_background_tile": True,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1062155885911425024/EMf90GZI_normal.jpg",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1062155885911425024/EMf90GZI_normal.jpg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/26257166/1526923497",
                "profile_link_color": "009999",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "EFEFEF",
                "profile_text_color": "333333",
                "profile_use_background_image": True,
                "has_extended_profile": False,
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None,
                "translator_type": "regular",
                "withheld_in_countries": []
            },
            "geo": None,
            "coordinates": None,
            "place": None,
            "contributors": None,
            "is_quote_status": False,
            "retweet_count": 4257,
            "favorite_count": 39312,
            "favorited": False,
            "retweeted": False,
            "possibly_sensitive": False,
            "lang": "en"
        },
        "is_quote_status": False,
        "retweet_count": 4257,
        "favorite_count": 0,
        "favorited": False,
        "retweeted": False,
        "possibly_sensitive": False,
        "lang": "en"
    },
    {
        "created_at": "Thu Feb 10 21:07:54 +0000 2022",
        "id": 1491881634311909400,
        "id_str": "1491881634311909377",
        "text":  "RT @JamalCollier: Bulls VP Arturas Karnisovas on Patrick Williams: At some point, you're going to see him this year Still says he doesn…",
        "truncated": False,
        "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [
                {
                    "screen_name": "JamalCollier",
                    "name": "Jamal Collier",
                    "id": 193172825,
                    "id_str": "193172825",
                    "indices": [
                        3,
                        16
                    ]
                }
            ],
            "urls": []
        },
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user": {
            "id": 50323173,
            "id_str": "50323173",
            "name": "Adrian Wojnarowski",
            "screen_name": "wojespn",
            "location": "St. Bonaventure, NY",
            "description": "ESPN Senior NBA Insider",
            "url": "https://t.co/BSi8UGrj5q",
            "entities": {
                "url": {
                    "urls": [
                        {
                            "url": "https://t.co/BSi8UGrj5q",
                            "expanded_url": "http://www.espn.com",
                            "display_url": "espn.com",
                            "indices": [
                                0,
                                23
                            ]
                        }
                    ]
                },
                "description": {
                    "urls": []
                }
            },
            "protected": False,
            "followers_count": 5207870,
            "friends_count": 1855,
            "listed_count": 34021,
            "created_at": "Wed Jun 24 14:43:40 +0000 2009",
            "favourites_count": 10108,
            "utc_offset": None,
            "time_zone": None,
            "geo_enabled": True,
            "verified": True,
            "statuses_count": 21758,
            "lang": None,
            "contributors_enabled": False,
            "is_translator": False,
            "is_translation_enabled": False,
            "profile_background_color": "642D8B",
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_tile": True,
            "profile_image_url": "http://pbs.twimg.com/profile_images/1264902234703265794/lC3YnIYF_normal.jpg",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/1264902234703265794/lC3YnIYF_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/50323173/1501272451",
            "profile_link_color": "FF0000",
            "profile_sidebar_border_color": "FFFFFF",
            "profile_sidebar_fill_color": "DDFFCC",
            "profile_text_color": "333333",
            "profile_use_background_image": True,
            "has_extended_profile": False,
            "default_profile": False,
            "default_profile_image": False,
            "following": None,
            "follow_request_sent": None,
            "notifications": None,
            "translator_type": "none",
            "withheld_in_countries": []
        },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "retweeted_status": {
            "created_at": "Thu Feb 10 21:07:06 +0000 2022",
            "id": 1491881433018863600,
            "id_str": "1491881433018863618",
            "text":  "RT @JamalCollier: Bulls VP Arturas Karnisovas on Patrick Williams: At some point, you're going to see him this year Still says he doesn…",
            "truncated": True,
            "entities": {
                "hashtags": [],
                "symbols": [],
                "user_mentions": [],
                "urls": [
                    {
                        "url": "https://t.co/PCBj6xOYD8",
                        "expanded_url": "https://twitter.com/i/web/status/1491881433018863618",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            116,
                            139
                        ]
                    }
                ]
            },
            "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user": {
                "id": 193172825,
                "id_str": "193172825",
                "name": "Jamal Collier",
                "screen_name": "JamalCollier",
                "location": "Chicago, IL.",
                "description": "I cover the NBA for @espn",
                "url": None,
                "entities": {
                    "description": {
                        "urls": []
                    }
                },
                "protected": False,
                "followers_count": 13887,
                "friends_count": 1160,
                "listed_count": 702,
                "created_at": "Tue Sep 21 04:21:41 +0000 2010",
                "favourites_count": 7101,
                "utc_offset": None,
                "time_zone": None,
                "geo_enabled": True,
                "verified": True,
                "statuses_count": 28164,
                "lang": None,
                "contributors_enabled": False,
                "is_translator": False,
                "is_translation_enabled": False,
                "profile_background_color": "131516",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
                "profile_background_tile": True,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1384097551058489347/HTXjkhdt_normal.jpg",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1384097551058489347/HTXjkhdt_normal.jpg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/193172825/1642738268",
                "profile_link_color": "0065B3",
                "profile_sidebar_border_color": "EEEEEE",
                "profile_sidebar_fill_color": "EFEFEF",
                "profile_text_color": "333333",
                "profile_use_background_image": True,
                "has_extended_profile": True,
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None,
                "translator_type": "none",
                "withheld_in_countries": []
            },
            "geo": None,
            "coordinates": None,
            "place": None,
            "contributors": None,
            "is_quote_status": False,
            "retweet_count": 263,
            "favorite_count": 3400,
            "favorited": False,
            "retweeted": False,
            "lang": "en"
        },
        "is_quote_status": False,
        "retweet_count": 263,
        "favorite_count": 0,
        "favorited": False,
        "retweeted": False,
        "lang": "en"
    },
    {
        "created_at": "Thu Feb 10 20:48:19 +0000 2022",
        "id": 1491876707833372700,
        "id_str": "1491876707833372678",
        "text": "Raptors are waiving Drew Eubanks, source tells ESPN. He arrived from Spurs in trade today.",
        "truncated": False,
        "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [],
            "urls": []
        },
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user": {
            "id": 50323173,
            "id_str": "50323173",
            "name": "Adrian Wojnarowski",
            "screen_name": "wojespn",
            "location": "St. Bonaventure, NY",
            "description": "ESPN Senior NBA Insider",
            "url": "https://t.co/BSi8UGrj5q",
            "entities": {
                "url": {
                    "urls": [
                        {
                            "url": "https://t.co/BSi8UGrj5q",
                            "expanded_url": "http://www.espn.com",
                            "display_url": "espn.com",
                            "indices": [
                                0,
                                23
                            ]
                        }
                    ]
                },
                "description": {
                    "urls": []
                }
            },
            "protected": False,
            "followers_count": 5207870,
            "friends_count": 1855,
            "listed_count": 34021,
            "created_at": "Wed Jun 24 14:43:40 +0000 2009",
            "favourites_count": 10108,
            "utc_offset": None,
            "time_zone": None,
            "geo_enabled": True,
            "verified": True,
            "statuses_count": 21758,
            "lang": None,
            "contributors_enabled": False,
            "is_translator": False,
            "is_translation_enabled": False,
            "profile_background_color": "642D8B",
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_tile": True,
            "profile_image_url": "http://pbs.twimg.com/profile_images/1264902234703265794/lC3YnIYF_normal.jpg",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/1264902234703265794/lC3YnIYF_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/50323173/1501272451",
            "profile_link_color": "FF0000",
            "profile_sidebar_border_color": "FFFFFF",
            "profile_sidebar_fill_color": "DDFFCC",
            "profile_text_color": "333333",
            "profile_use_background_image": True,
            "has_extended_profile": False,
            "default_profile": False,
            "default_profile_image": False,
            "following": None,
            "follow_request_sent": None,
            "notifications": None,
            "translator_type": "none",
            "withheld_in_countries": []
        },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "is_quote_status": False,
        "retweet_count": 728,
        "favorite_count": 8966,
        "favorited": False,
        "retweeted": False,
        "lang": "en"
    },
    {
        "created_at": "Thu Feb 10 20:18:58 +0000 2022",
        "id": 1491869320946802700,
        "id_str": "1491869320946802688",
        "text": "Ben Simmons has already talked to Kevin Durant and Sean Marks, @KlutchSports' Rich Paul tells ESPN. Simmons is eage… https://t.co/KwUj4MJa8K",
        "truncated": True,
        "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [
                {
                    "screen_name": "KlutchSports",
                    "name": "Klutch Sports Group",
                    "id": 848666563,
                    "id_str": "848666563",
                    "indices": [
                        63,
                        76
                    ]
                }
            ],
            "urls": [
                {
                    "url": "https://t.co/KwUj4MJa8K",
                    "expanded_url": "https://twitter.com/i/web/status/1491869320946802688",
                    "display_url": "twitter.com/i/web/status/1…",
                    "indices": [
                        117,
                        140
                    ]
                }
            ]
        },
        "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user": {
            "id": 50323173,
            "id_str": "50323173",
            "name": "Adrian Wojnarowski",
            "screen_name": "wojespn",
            "location": "St. Bonaventure, NY",
            "description": "ESPN Senior NBA Insider",
            "url": "https://t.co/BSi8UGrj5q",
            "entities": {
                "url": {
                    "urls": [
                        {
                            "url": "https://t.co/BSi8UGrj5q",
                            "expanded_url": "http://www.espn.com",
                            "display_url": "espn.com",
                            "indices": [
                                0,
                                23
                            ]
                        }
                    ]
                },
                "description": {
                    "urls": []
                }
            },
            "protected": False,
            "followers_count": 5207870,
            "friends_count": 1855,
            "listed_count": 34021,
            "created_at": "Wed Jun 24 14:43:40 +0000 2009",
            "favourites_count": 10108,
            "utc_offset": None,
            "time_zone": None,
            "geo_enabled": True,
            "verified": True,
            "statuses_count": 21758,
            "lang": None,
            "contributors_enabled": False,
            "is_translator": False,
            "is_translation_enabled": False,
            "profile_background_color": "642D8B",
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_tile": True,
            "profile_image_url": "http://pbs.twimg.com/profile_images/1264902234703265794/lC3YnIYF_normal.jpg",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/1264902234703265794/lC3YnIYF_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/50323173/1501272451",
            "profile_link_color": "FF0000",
            "profile_sidebar_border_color": "FFFFFF",
            "profile_sidebar_fill_color": "DDFFCC",
            "profile_text_color": "333333",
            "profile_use_background_image": True,
            "has_extended_profile": False,
            "default_profile": False,
            "default_profile_image": False,
            "following": None,
            "follow_request_sent": None,
            "notifications": None,
            "translator_type": "none",
            "withheld_in_countries": []
        },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "is_quote_status": False,
        "retweet_count": 2539,
        "favorite_count": 26095,
        "favorited": False,
        "retweeted": False,
        "lang": "en"
    }
]

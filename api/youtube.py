import requests


class Youtube:
    def __init__(self):
        self.headers = {
            'authority': 'www.youtube.com',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-bitness': '"64"',
            'x-youtube-bootstrap-logged-in': 'false',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-full-version': '"97.0.4692.71"',
            'sec-ch-ua-platform-version': '"5.13.0"',
            'x-youtube-client-name': '1',
            'x-youtube-client-version': '2.20220629.01.00',
            'x-goog-visitor-id': 'CgtsZjZLV0FyaFAyRSjX-vWVBg%3D%3D',
            'sec-ch-ua-platform': '"Linux"',
            'accept': '*/*',
            'origin': 'https://www.youtube.com',
            'x-client-data': 'CIa2yQEIorbJAQipncoBCLCNywEIlqHLARirqcoB',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'same-origin',
            'sec-fetch-dest': 'empty',
            'accept-language': 'en-US,en;q=0.9',
        }

        self.params = {
            'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
            'prettyPrint': 'false',
        }

    def search(self, query):
        json_data = {
            'context': {
                'client': {
                    'hl': 'en',
                    'gl': 'PK',
                    'remoteHost': '103.7.79.74',
                    'deviceMake': '',
                    'deviceModel': '',
                    'visitorData': 'CgtsZjZLV0FyaFAyRSjX-vWVBg%3D%3D',
                    'userAgent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.0.0 Safari/537.36,gzip(gfe)',
                    'clientName': 'WEB',
                    'clientVersion': '2.20220629.01.00',
                    'osName': 'X11',
                    'osVersion': '',
                    'originalUrl': 'https://www.youtube.com/results?search_query=fallguys+jayplays',
                    'platform': 'DESKTOP',
                    'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                    'configInfo': {
                        'appInstallData': 'CNf69ZUGEK6ergUQt8utBRDUg64FEJje_RIQz_L9EhCjpa4FELiLrgUQ8JmuBRCB8v0SENi-rQUQkfj8Eg%3D%3D',
                    },
                    'timeZone': 'Asia/Karachi',
                    'browserName': 'Chrome',
                    'browserVersion': '97.0.0.0',
                    'screenWidthPoints': 1208,
                    'screenHeightPoints': 413,
                    'screenPixelDensity': 1,
                    'screenDensityFloat': 1,
                    'utcOffsetMinutes': 300,
                    'userInterfaceTheme': 'USER_INTERFACE_THEME_LIGHT',
                    'memoryTotalKbytes': '8000000',
                    'mainAppWebInfo': {
                        'graftUrl': '/results?search_query=fallguys+jayplays',
                        'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED',
                        'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                        'isWebNativeShareAvailable': False,
                    },
                },
                'user': {
                    'lockedSafetyMode': False,
                },
                'request': {
                    'useSsl': True,
                    'internalExperimentFlags': [],
                    'consistencyTokenJars': [],
                },
                'clickTracking': {
                    'clickTrackingParams': 'CBYQ7VAiEwiDhtSO_tT4AhXXUw8CHaFoDVI=',
                },
                'adSignalsInfo': {
                    'params': [
                        {
                            'key': 'dt',
                            'value': '1656585562116',
                        },
                        {
                            'key': 'flash',
                            'value': '0',
                        },
                        {
                            'key': 'frm',
                            'value': '0',
                        },
                        {
                            'key': 'u_tz',
                            'value': '300',
                        },
                        {
                            'key': 'u_his',
                            'value': '2',
                        },
                        {
                            'key': 'u_h',
                            'value': '1024',
                        },
                        {
                            'key': 'u_w',
                            'value': '1280',
                        },
                        {
                            'key': 'u_ah',
                            'value': '997',
                        },
                        {
                            'key': 'u_aw',
                            'value': '1208',
                        },
                        {
                            'key': 'u_cd',
                            'value': '24',
                        },
                        {
                            'key': 'bc',
                            'value': '31',
                        },
                        {
                            'key': 'bih',
                            'value': '413',
                        },
                        {
                            'key': 'biw',
                            'value': '1192',
                        },
                        {
                            'key': 'brdim',
                            'value': '72,27,72,27,1208,27,1208,997,1208,413',
                        },
                        {
                            'key': 'vis',
                            'value': '1',
                        },
                        {
                            'key': 'wgl',
                            'value': 'true',
                        },
                        {
                            'key': 'ca_type',
                            'value': 'image',
                        },
                    ],
                    'bid': 'ANyPxKobCL2XzQHJhgbyXjP3nRfO1_FxWY2yF8QlawPBKqbou8QK3sxb1r6s202LJ1GvuoPeqhp5UA3pBfEo-1wa6VOw77GdbA',
                },
            },
            'query': f'{query}',
            'webSearchboxStatsUrl': f'/search?oq={query}&gs_l=youtube.12..0i30i22k1.4009.7367.0.11547.18.12.0.0.0.0.861.2263.5-1j2.4.0.qsjkc2,ytpo-bo-me=0,ytposo-bo-me=0,ytpo-bo-mq=1500,ytpo-bo-vo-mq=1500,ytpo-bo-ro-e=1,ytpo-bo-ro-el=1,ytpo-bo-ro-er=1,ytpo-bo-ro-erps=1,ytpo-bo-ro-erns=1,ytpo-bo-ro-erp=1,ytpo-bo-ro-ern=1,ytpo-bo-ro-mp=1500,ytpo-bo-ro-mn=1500,ytpo-bo-ro-mq=0,ytpo-bo-ro-mps=1500,ytpo-bo-ro-mns=1500,ytpo-bo-ro-mqs=0,ytpo-bo-ro-unf=1000000000,ytpo-bo-ro-mi=24215972,ytposo-bo-mq=1500,ytposo-bo-vo-mq=1500,ytposo-bo-ro-e=1,ytposo-bo-ro-el=1,ytposo-bo-ro-er=1,ytposo-bo-ro-erps=1,ytposo-bo-ro-erns=1,ytposo-bo-ro-erp=1,ytposo-bo-ro-ern=1,ytposo-bo-ro-mp=1500,ytposo-bo-ro-mn=1500,ytposo-bo-ro-mq=0,ytposo-bo-ro-mps=1500,ytposo-bo-ro-mns=1500,ytposo-bo-ro-mqs=0,ytposo-bo-ro-unf=1000000000,ytposo-bo-ro-mi=24215972,cfro=1,ytpo-bo-me=1,ytposo-bo-me=1,ytpo-bo-uo-et=1,ytposo-bo-uo-et=1,ytpo-bo-mq=1500,ytpo-bo-vo-mq=1500,ytpo-bo-ro-e=1,ytpo-bo-ro-el=1,ytpo-bo-ro-er=1,ytpo-bo-ro-erps=1,ytpo-bo-ro-erns=1,ytpo-bo-ro-erp=1,ytpo-bo-ro-ern=1,ytpo-bo-ro-mp=1500,ytpo-bo-ro-mn=1500,ytpo-bo-ro-mq=0,ytpo-bo-ro-mps=1500,ytpo-bo-ro-mns=1500,ytpo-bo-ro-mqs=0,ytpo-bo-ro-unf=1000000000,ytpo-bo-ro-mi=24215972,ytposo-bo-mq=1500,ytposo-bo-vo-mq=1500,ytposo-bo-ro-e=1,ytposo-bo-ro-el=1,ytposo-bo-ro-er=1,ytposo-bo-ro-erps=1,ytposo-bo-ro-erns=1,ytposo-bo-ro-erp=1,ytposo-bo-ro-ern=1,ytposo-bo-ro-mp=1500,ytposo-bo-ro-mn=1500,ytposo-bo-ro-mq=0,ytposo-bo-ro-mps=1500,ytposo-bo-ro-mns=1500,ytposo-bo-ro-mqs=0,ytposo-bo-ro-unf=1000000000,ytposo-bo-ro-mi=24215972...0...1ac.1.64.youtube..14.3.2262.0..0i471k1j0i512i433i131k1j0i433i131k1j0i13k1.1016.t0RoQC0wisQ',
        }

        response = requests.post('https://www.youtube.com/youtubei/v1/search',
                                 params=self.params, headers=self.headers, json=json_data).json()
        return response

    def stripText(self, text):
        text = text[:23]
        return text+"......"

    def videos(self, response):
        datastore = []
        contents = response['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents']
        video_contents = contents[0]['itemSectionRenderer']['contents']
        for video_id in range(1, len(video_contents)):
            try:
                video_content = video_contents[video_id]['videoRenderer']
                channel_img = video_content['channelThumbnailSupportedRenderers'][
                    'channelThumbnailWithLinkRenderer']['thumbnail']['thumbnails'][0]['url']
                owner_name = video_content['ownerText']['runs'][0]['text']
                video_views = video_content['viewCountText']['simpleText']
                pub_date = video_content['publishedTimeText']['simpleText']
                video_thumb = video_content['thumbnail']['thumbnails'][0]['url']
                video_title = video_content['title']['runs'][0]['text']
                video_id = video_content['videoId']

                datastore.append({
                    "channel_img": channel_img,
                    "owner_name": owner_name,
                    "video_views": video_views,
                    "pub_date": pub_date,
                    "video_thumb": video_thumb,
                    "video_title": self.stripText(video_title),
                    "video_id": video_id,
                    "main_title": video_title
                })
            except:
                print("No data present at {}.".format(video_id))
        return datastore

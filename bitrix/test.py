import js2py

code = '''var d = new Date();
        d.setDate(date.getDate() + 7);
        d.setSeconds(0);
        var dateStr = d.getFullYear() + '-' + paddatepart(1 + d.getMonth()) + '-' + paddatepart(d.getDate()) + 'T' + paddatepart(d.getHours()) + ':'
                     + paddatepart(d.getMinutes()) + ':' + paddatepart(d.getSeconds()) + '+00:00';
                var paddatepart = function(part)
                {
                     return part >= 10 ? part.toString() : '0' + part.toString();
                }

        BX24.callMethod(
            "crm.activity.add",
            {
                fields:
                {
                                        "OWNER_TYPE_ID": 2, //from the method crm.enum.ownertype: 2 - "activity" type
                    "OWNER_ID": 102, //activity ID
                    "TYPE_ID": 2, // see crm.enum.activitytype
                    "COMMUNICATIONS": [ { VALUE:"+75555555051", ENTITY_ID:134,ENTITY_TYPE_ID:3 } ], //where 134 - contract id, 3 - "contact" type
                    "SUBJECT": "New call",
                    "START_TIME": dateStr,
                    "END_TIME": dateStr,
                    "COMPLETED": "N",
                    "PRIORITY": 3, // see crm.enum.activitypriority
                    "RESPONSIBLE_ID": 1,
                    "DESCRIPTION": "Important call",
                    "DESCRIPTION_TYPE": 3, // see crm.enum.contenttype
                                        "DIRECTION": 2, // see crm.enum.activitydirection
                            "WEBDAV_ELEMENTS":
                                    [
                                        { fileData: document.getElementById('file1') }
                                    ],
                    "FILES":
                                    [
                                        { fileData: document.getElementById('file1') }
      ] //after disk module is installed and converted from webdav, FILES can be specified instead of WEBDAV_ELEMENTS
                }
            },
            function(result)
            {
                if(result.error())
                    console.error(result.error());
                else
                    console.info("New call with ID is created " + result.data());
            }
        );'''

f = js2py.eval_js(code)

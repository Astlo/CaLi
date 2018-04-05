ACTIONS = ["Attribution", "CommercialUse", "DerivativeWorks", "Distribution", "Notice", "Reproduction", "ShareAlike", "Sharing", "SourceCode", "acceptTracking", "adHocShare", "aggregate", "annotate", "anonymize", "append", "appendTo", "archive", "attachPolicy", "attachSource", "attribute", "commercialize", "compensate", "concurrentUse", "copy", "delete", "derive", "digitize", "display", "distribute", "ensureExclusivity", "execute", "export", "extract", "extractChar", "extractPage", "extractWord", "give", "grantUse", "include", "index", "inform", "install", "lease", "lend", "license", "modify", "move", "nextPolicy", "obtainConsent", "pay", "play", "present", "preview", "print", "read", "reproduce", "reviewPolicy", "secondaryUse", "sell", "share", "shareAlike", "stream", "synchronize", "textToSpeech", "transfer", "transform", "translate", "uninstall", "use", "watermark", "write", "writeTo"]

ATTRIBUTION = "Attribution"

COMMERCIALUSE = "CommercialUse"

DERIVATIVE_WORKS = "DerivativeWorks"

DISTRIBUTION =  "Distribution"

NOTICE = "Notice"

REPRODUCTION = "Reproduction"

SHARE_ALIKE = "ShareAlike"

CONCURRENTUSE = "concurrentUse"

USE = 'use'

ARBRE = [{
    'name' : USE,
    'includedIn' : [{
        'name' : REPRODUCE,
        'includedIn' : [{
            'name' : REPRODUCTION,
            'includedIn' : [{
                'name' : CONCURRENTUSE,
                'includedIn' : []
            }, {
               'name' : DIGITIZE,
               'includedIn' : []
            }]
        }]
     }, {
        'name' : MOVE,
        'includedIn' : [{
           'name' : DELETE,
           'includedIn' : []
        }]
     }, {
        'name' : SHARING,
        'includedIn' : [ARBRE_DERIVE]
     }, {
        'name' : DERIVATIVE_WORKS,
        'includedIn' : [{
           'name' : DISTRIBUTION,
           'includedIn' : [{
              'name' : DISTRIBUTE,
              'includedIn' : []
           }]
        }, ARBRE_DERIVE]
     }, {
        'name' : MODIFY,
        'includedIn' : [{
           'name' : ANNOTATE,
           'includedIn' : []
        }, {
           'name' : ,
           'includedIn' : []
        }]
     }]
}, {
   'name' : TRANSFER,
   'includedIn' : [{
      'name' : GIVE,
      'includedIn' : []
   }, {
      'name' : SELL,
      'includedIn' : []
   }]
}]

ARBRE_DERIVE = {
   'name' : DERIVE,
   'includedIn' : [{
      'name' : PRINT,
      'includedIn' : []
   }, {
      'name' : PLAY,
      'includedIn' : [{
         'name' : DISPLAY,
         'includedIn' : []
      }]
   }]
}

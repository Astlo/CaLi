ACTIONS = ["Attribution", "CommercialUse", "DerivativeWorks", "Distribution", "Notice", "Reproduction", "ShareAlike", "Sharing", "SourceCode", "acceptTracking", "adHocShare", "aggregate", "annotate", "anonymize", "append", "appendTo", "archive", "attachPolicy", "attachSource", "attribute", "commercialize", "compensate", "concurrentUse", "copy", "delete", "derive", "digitize", "display", "distribute", "ensureExclusivity", "execute", "export", "extract", "extractChar", "extractPage", "extractWord", "give", "grantUse", "include", "index", "inform", "install", "lease", "lend", "license", "modify", "move", "nextPolicy", "obtainConsent", "pay", "play", "present", "preview", "print", "read", "reproduce", "reviewPolicy", "secondaryUse", "sell", "share", "shareAlike", "stream", "synchronize", "textToSpeech", "transfer", "transform", "translate", "uninstall", "use", "watermark", "write", "writeTo"]

ATTRIBUTION = "Attribution"

COMMERCIALUSE = "CommercialUse"

DERIVATIVE_WORKS = "DerivativeWorks"

DISTRIBUTION =  "Distribution"

NOTICE = "Notice"

REPRODUCTION = "Reproduction"

SHARE_ALIKE = "ShareAlike"

SHARING = "Sharing"

SOURCECODE = "SourceCode"

ACCEPTTRACKING = "acceptTracking"

AGGREGATE = "aggregate"

ANNOTATE = "annotate"

ANONYMIZE = "anonymize"

ARCHIVE = "archive"

ATTRIBUTE = "attribute"

COMPENSATE = "compensate"

CONCURRENTUSE = "concurrentUse"

DELETE = "delete"

DERIVE = "derive"

DIGITIZE = "digitize"

DISTRIBUTE = "distribute"

ENSUREEXCLUSIVITY = "ensureExclusivity"

EXECUTE = "execute"

EXTRACT = "extract"

GIVE = "give"

GRANTUSE = "grantUse"

INCLUDE = "include"

INDEX = "index"

INFORM = "INFORM"

INSTALL = "install"

MODIFY = "modify"

MOVE = "move"

NEXTPOLICY = "nextPolicy"

OBTAINCONSENT = "obtainConsent"

PLAY = "play"

PRESENT = "present"

PRINT = "print"

READ = "read"

REPRODUCE = "reproduce"

REVIEWPOLICY = "reviewPolicy"

SELL = "sell"

STREAM = "stream"

SYNCHRONIZE = "synchronize"

TEXTTOSPEECH = "textToSpeech"

TRANSFER = "transfer"

TRANSFORM = "transform"

TRANSLATE = "translate"

UNINSTALL = "uninstall"

WATERMARK = "watermark"


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
           }, {
              'name' : PRESENT,
              'includedIn' : []
           }, {
              'name' : STREAM,
              'includedIn' : []
           }, {
              'name' : TEXTTOSPEECH,
              'includedIn' : []
           }]
        }, ARBRE_DERIVE]
     }, {
        'name' : MODIFY,
        'includedIn' : [{
           'name' : ANONYMIZE,
           'includedIn' : []
        }, {
           'name' : ,
           'includedIn' : []
        }]
     }, {
        'name' : COMMERCIALUSE,
        'includedIn' : []
     }, {
        'name' : NOTICE,
        'includedIn' : []
     }, {
        'name' : SOURCECODE,
        'includedIn' : []
     }, {
        'name' : ACCEPTTRACKING,
        'includedIn' : []
     }, {
        'name' : ARCHIVE,
        'includedIn' : []
     }, {
        'name' : ATTRIBUTE,
        'includedIn' : []
     }, {
        'name' : ENSUREEXCLUSIVITY,
        'includedIn' : []
     }, {
        'name' : EXECUTE,
        'includedIn' : []
     }, {
        'name' : GRANTUSE,
        'includedIn' : []
     }, {
        'name' : INCLUDE,
        'includedIn' : []
     }, {
        'name' : INDEX,
        'includedIn' : []
     }, {
        'name' : INFORM,
        'includedIn' : []
     }, {
        'name' : INSTALL,
        'includedIn' : []
     }, {
        'name' : NEXTPOLICY,
        'includedIn' : []
     }, {
        'name' : OBTAINCONSENT,
        'includedIn' : []
     }, {
        'name' : READ,
        'includedIn' : []
     }, {
        'name' : REVIEWPOLICY,
        'includedIn' : []
     }, {
        'name' : TRANSLATE,
        'includedIn' : []
     }, {
        'name' : UNINSTALL,
        'includedIn' : []
     }, {
        'name' : WATERMARK,
        'includedIn' : []
     }, {
        'name' : ,
        'includedIn' : []
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

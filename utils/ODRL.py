ACTIONS = ["Attribution", "CommericalUse", "DerivativeWorks", "Distribution", "Notice", "Reproduction", "ShareAlike", "Sharing", "SourceCode", "acceptTracking", "adHocShare", "aggregate", "annotate", "anonymize", "append", "appendTo", "archive", "attachPolicy", "attachSource", "attribute", "commercialize", "compensate", "concurrentUse", "copy", "delete", "derive", "digitize", "display", "distribute", "ensureExclusivity", "execute", "export", "extract", "extractChar", "extractPage", "extractWord", "give", "grantUse", "include", "index", "inform", "install", "lease", "lend", "license", "modify", "move", "nextPolicy", "obtainConsent", "pay", "play", "present", "preview", "print", "read", "reproduce", "reviewPolicy", "secondaryUse", "sell", "share", "stream", "synchronize", "textToSpeech", "transfer", "transform", "translate", "uninstall", "use", "watermark", "write", "writeTo"]

ATTRIBUTION = "Attribution"

COMMERCIALUSE = "CommericalUse"

DERIVATIVE_WORKS = "DerivativeWorks"

DISTRIBUTION = "Distribution"

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

DISPLAY = "display"

DISTRIBUTE = "distribute"

ENSUREEXCLUSIVITY = "ensureExclusivity"

EXECUTE = "execute"

EXTRACT = "extract"

GIVE = "give"

GRANTUSE = "grantUse"

INCLUDE = "include"

INDEX = "index"

INFORM = "inform"

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

USE = "use"

ARBRE_DERIVE =
   DERIVE: {
      PRINT: {},
      PLAY: {
         DISPLAY: {}
      }
   }


ARBRE = {
    USE: {
        REPRODUCE: {
            REPRODUCTION: {
                CONCURRENTUSE: {},
                DIGITIZE: {}
            }
        },
        MOVE: {
           DELETE: {}
        },
        SHARING: {
            ARBRE_DERIVE
        },
        DERIVATIVE_WORKS: {
            ARBRE_DERIVE,
            SHARE_ALIKE: {}
        },
        DISTRIBUTION: {
            DISTRIBUTE: {},
            PRESENT: {},
            STREAM: {},
            TEXTTOSPEECH: {}
        },
        MODIFY: {
            ANONYMIZE: {},
            TRANSFORM: {}
        },
        COMMERCIALUSE: {},
        NOTICE: {},
        SOURCECODE: {},
        ACCEPTTRACKING: {},
        AGGREGATE: {},
        ANNOTATE: {},
        ARCHIVE: {},
        ATTRIBUTE: {},
        ATTRIBUTION: {},
        COMPENSATE: {},
        ENSUREEXCLUSIVITY: {},
        EXECUTE: {},
        EXTRACT: {},
        GRANTUSE: {},
        INCLUDE: {},
        INDEX: {},
        INFORM: {},
        INSTALL: {},
        NEXTPOLICY: {},
        OBTAINCONSENT: {},
        READ: {},
        REVIEWPOLICY: {},
        SYNCHRONIZE: {},
        TRANSFORM: {},
        TRANSLATE: {},
        UNINSTALL: {},
        WATERMARK: {},
        TRANSFER: {
            GIVE: {},
            SELL: {}
        }
    }
}

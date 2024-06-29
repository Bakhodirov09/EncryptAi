import org.zaproxy.zap.extension.script.SimpleScript
import org.zaproxy.zap.extension.script.ScriptVars
import org.zaproxy.zap.extension.script.ZapApi
import org.zaproxy.zap.extension.script.ScriptParams

class InstagramXSS extends SimpleScript {

    ScriptParams params
    ScriptVars vars
    def api

    @Override
    def init(params, context, targets) {
        this.params = params
        this.vars = context.getVariableContext()
        this.api = context.getApi()
    }

    @Override
    def scan(target) {
        def url = target.url.toString()
        if (url.contains("/profile.php")) {
            api.spider.scan(url, "GET", new String[0])
            def alerts = api.alert.getAlerts(url)
            for (alert in alerts) {
                def evidence = alert.getEvidence()
                if (evidence.contains("script") || evidence.contains("iframe")) {
                    vars.add(vars.get("vulnerable_urls"), url)
                }
            }
        }
    }
}
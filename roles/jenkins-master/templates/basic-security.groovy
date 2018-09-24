// Create the admin user account if it doesn't already exist.
if ("{{ jenkins_admin_username }}" in users_s) {
    println "Admin user already exists"
    println "Admin user already exists - updating password"
     def user = hudson.model.User.get('{{ jenkins_admin_username }}');
    def password = hudson.security.HudsonPrivateSecurityRealm.Details.fromPlainPassword('{{ jenkins_admin_password }}')
    user.addProperty(password)
    user.save()
}
else {
    println "--> creating local admin user"

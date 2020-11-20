from vespa.package import Document, Field

document = Document(
    fields=[
        Field(name = "id", type = "string", indexing = ["attribute", "summary"]),
        Field(name = "title", type = "string", indexing = ["index", "summary"], index = "enable-bm25"),
        Field(name = "body", type = "string", indexing = ["index", "summary"], index = "enable-bm25")
    ]
)


from vespa.package import Schema, FieldSet, RankProfile

msmarco_schema = Schema(
    name = "msmarco",
    document = document,
    fieldsets = [FieldSet(name = "default", fields = ["title", "body"])],
    rank_profiles = [RankProfile(name = "default", first_phase = "nativeRank(title, body)")]
)

from vespa.package import ApplicationPackage

app_package = ApplicationPackage(name = "msmarco", schema=msmarco_schema)

from vespa.package import VespaDocker

path = "C:/Users/User/OneDrive - NTNU/NTNU/Prosjekt oppgave NLP/"
name = "test_app/"

app_path = path + name

vespa_docker = VespaDocker()
vespa_docker.deploy(application_package=app_package, disk_folder = app_path)
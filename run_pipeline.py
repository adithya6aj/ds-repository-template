from databricks import sdk
from databricks.sdk.service.jobs import NotebookTask, Task, TaskDependency

# Initialize the Databricks SDK client
client = sdk.WorkspaceClient()

# Define the notebook paths
ingestion_notebook_path = "/Users/athithya.raj@trinitypartners.com/IrisPipeline/data_ingestion"
eda_notebook_path = "/Users/athithya.raj@trinitypartners.com/IrisPipeline/eda"
feature_engineering_notebook_path = "/Users/athithya.raj@trinitypartners.com/IrisPipeline/feature_engineering"
training_notebook_path = "/Users/athithya.raj@trinitypartners.com/IrisPipeline/training"
inference_notebook_path = "/Users/athithya.raj@trinitypartners.com/IrisPipeline/inference"

# Create a new Databricks Job
job = client.jobs.create(
    name="Iris Data Pipeline",
    tasks=[
        Task(
            task_key="ingestion",
            notebook_task=NotebookTask(notebook_path=ingestion_notebook_path),
        ),
        Task(
            task_key="eda",
            depends_on=[TaskDependency(task_key="ingestion")],
            notebook_task=NotebookTask(notebook_path=eda_notebook_path),
        ),
        Task(
            task_key="feature_engineering",
            depends_on=[TaskDependency(task_key="eda")],
            notebook_task=NotebookTask(notebook_path=feature_engineering_notebook_path),
        ),
        Task(
            task_key="training",
            depends_on=[TaskDependency(task_key="feature_engineering")],
            notebook_task=NotebookTask(notebook_path=training_notebook_path),
        ),
        Task(
            task_key="inference",
            depends_on=[TaskDependency(task_key="training")],
            notebook_task=NotebookTask(notebook_path=inference_notebook_path),
        ),
    ],
)

print(f"Created Databricks Job with ID: {job.job_id}")
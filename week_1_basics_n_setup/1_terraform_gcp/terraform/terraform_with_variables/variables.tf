#variable "credentials" {
#  description = "My Credentials"
#  default     = "C:/Users/jwebb/Git Repos/data-engineering-zoomcamp/week_1_basics_n_setup/1_terraform_gcp/terraform/terraform_with_variables/de-johnwebb-3fddbf4c0b9c.json"
#  #ex: if you have a directory where this file is called keys with your service account json file
#  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
#}


variable "project" {
  description = "Project"
  default     = "de-johnwebb"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "us-west3-a"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default     = "terraform-demo-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
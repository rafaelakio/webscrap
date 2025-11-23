variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "webscrap"
}

variable "uol_email" {
  description = "UOL email for login"
  type        = string
  sensitive   = true
}

variable "uol_password" {
  description = "UOL password for login"
  type        = string
  sensitive   = true
}

variable "enable_schedule" {
  description = "Enable scheduled execution"
  type        = bool
  default     = false
}

variable "schedule_expression" {
  description = "Schedule expression for EventBridge (e.g., rate(1 hour))"
  type        = string
  default     = "rate(1 hour)"
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default = {
    Project     = "webscrap"
    Environment = "dev"
    ManagedBy   = "Terraform"
  }
}

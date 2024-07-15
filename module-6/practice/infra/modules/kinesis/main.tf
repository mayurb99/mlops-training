resource "aws_kinesis_stream" "test_stream" {
  name             = var.stream_name
  shard_count      = var.shard_count
  retention_period = var.retention_period

  shard_level_metrics = var.shard_level_metrics

  
}

output "stream_arn" {
  value = aws_kinesis_stream.test_stream.arn
}
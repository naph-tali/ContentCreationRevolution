#  DEEPSEEK API INTEGRATION MODULE

$DeepSeekAPI = @{
    BaseURL = \"https://api.deepseek.com\"
    Version = \"v1\"
    Endpoints = @{
        Chat = \"/chat/completions\"
        Models = \"/models\" 
        Embeddings = \"/embeddings\"
    }
}

class DeepSeekClient {
    [string]$ApiKey
    [string]$BaseURL
    [hashtable]$Headers
    
    DeepSeekClient([string]$apiKey) {
        $this.ApiKey = $apiKey
        $this.BaseURL = $DeepSeekAPI.BaseURL
        $this.Headers = @{
            \"Authorization\" = \"Bearer $apiKey\"
            \"Content-Type\" = \"application/json\"
        }
    }
    
    [psobject] ChatCompletion([hashtable]$messages, [string]$model = \"deepseek-chat\") {
        $body = @{
            model = $model
            messages = $messages
            stream = $false
        } | ConvertTo-Json -Depth 10
        
        try {
            $response = Invoke-RestMethod -Uri \"$($this.BaseURL)$($DeepSeekAPI.Endpoints.Chat)\" -Method Post -Headers $this.Headers -Body $body
            return $response
        } catch {
            Write-Error \"DeepSeek API Error: $($_.Exception.Message)\"
            return $null
        }
    }
    
    [psobject] GetModels() {
        try {
            $response = Invoke-RestMethod -Uri \"$($this.BaseURL)$($DeepSeekAPI.Endpoints.Models)\" -Method Get -Headers $this.Headers
            return $response
        } catch {
            Write-Error \"DeepSeek API Error: $($_.Exception.Message)\"
            return $null
        }
    }
}

function Initialize-DeepSeek {
    param([string]$ApiKey)
    
    if (-not $ApiKey) {
        Write-Host \" DeepSeek API Key not provided\" -ForegroundColor Red
        return $null
    }
    
    $client = [DeepSeekClient]::new($ApiKey)
    Write-Host \" DeepSeek API Client Initialized\" -ForegroundColor Green
    return $client
}

function Get-DeepSeekAdvice {
    param(
        [DeepSeekClient]$Client,
        [string]$Context,
        [string]$Question
    )
    
    $messages = @(
        @{
            role = \"system\"
            content = \"You are an AI assistant helping with the Content Creation Revolution project. Provide concise, actionable advice.\"
        },
        @{
            role = \"user\" 
            content = \"Project Context: $Context 
Question: $Question\"
        }
    )
    
    $response = $Client.ChatCompletion($messages)
    if ($response -and $response.choices) {
        return $response.choices[0].message.content
    }
    
    return \"Unable to get DeepSeek advice at this time.\"
}

function Optimize-ContentWithDeepSeek {
    param(
        [DeepSeekClient]$Client,
        [string]$Content,
        [string]$Platform = \"twitter\"
    )
    
    $messages = @(
        @{
            role = \"system\"
            content = \"You are a content optimization expert. Optimize the given content for the specified platform while maintaining the core message and revolutionary spirit.\"
        },
        @{
            role = \"user\"
            content = \"Platform: $Platform 
Content to optimize: $Content\"
        }
    )
    
    $response = $Client.ChatCompletion($messages)
    if ($response -and $response.choices) {
        return $response.choices[0].message.content
    }
    
    return $Content
}

function Analyze-EngagementPatterns {
    param(
        [DeepSeekClient]$Client,
        [array]$TweetHistory
    )
    
    $analysisPrompt = @\"
Analyze these tweet engagement patterns and suggest improvements:

Tweet History:
$($TweetHistory | ConvertTo-Json -Depth 2)

Provide specific recommendations for:
1. Content themes that perform well
2. Optimal posting times
3. Engagement strategies
4. Content format improvements
\"@

    $messages = @(
        @{
            role = \"system\" 
            content = \"You are a social media analytics expert. Analyze engagement patterns and provide data-driven recommendations.\"
        },
        @{
            role = \"user\"
            content = $analysisPrompt
        }
    )
    
    $response = $Client.ChatCompletion($messages)
    return $response.choices[0].message.content
}

# Export functions
Export-ModuleMember -Function Initialize-DeepSeek, Get-DeepSeekAdvice, Optimize-ContentWithDeepSeek, Analyze-EngagementPatterns
